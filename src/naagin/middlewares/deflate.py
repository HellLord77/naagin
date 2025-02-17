from typing import override
from zlib import Z_DEFAULT_COMPRESSION
from zlib import compressobj
from zlib import decompressobj

from fastapi.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp

from naagin.abstract import BaseEncoding
from naagin.abstract import BaseEncodingMiddleware
from naagin.enums import EncodingEnum
from naagin.utils import DOAXVVHeader
from naagin.utils.encodings.decoder import DecompressFlushDecoder
from naagin.utils.encodings.encoder import CompressFlushEncoder


class DeflateMiddleware(BaseEncodingMiddleware):
    send_header = DOAXVVHeader("Encoding")
    receive_header = str(send_header)

    @override
    def __init__(self, app: ASGIApp, *, send_encoded: bool = True, compress_level: int = Z_DEFAULT_COMPRESSION) -> None:
        super().__init__(app, send_encoded=send_encoded)
        self.compress_level = compress_level

    def is_receive_encoding_set(self, headers: Headers) -> bool:
        return EncodingEnum.DEFLATE in headers.getlist(self.receive_header)

    async def get_receive_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        del headers[self.receive_header]
        return DecompressFlushDecoder(decompressobj())

    def is_send_encoding_set(self, headers: Headers) -> bool:
        return EncodingEnum.DEFLATE in headers.getlist(self.send_header)

    async def get_send_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        headers[self.send_header] = EncodingEnum.DEFLATE
        return CompressFlushEncoder(compressobj(self.compress_level))
