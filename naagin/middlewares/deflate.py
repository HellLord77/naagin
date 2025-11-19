from typing import override
from zlib import Z_DEFAULT_COMPRESSION
from zlib import compressobj
from zlib import decompressobj

from starlette.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp

from naagin.abstract import BaseEncodingMiddleware
from naagin.enums import DOAXVVHeaderEnum
from naagin.enums import EncodingEnum
from naagin.types_ import ZLibCompressor
from naagin.types_ import ZLibDecompressor
from naagin.utils import DOAXVVHeader


class DeflateMiddleware(BaseEncodingMiddleware):
    decompressor: ZLibDecompressor
    compressor: ZLibCompressor

    header = DOAXVVHeaderEnum.ENCODING

    @override
    def __init__(self, app: ASGIApp, *, send_encoded: bool = True, compress_level: int = Z_DEFAULT_COMPRESSION) -> None:
        super().__init__(app, send_encoded=send_encoded)
        self.compress_level = compress_level

    def should_receive_with_decoder(self, headers: Headers) -> bool:
        return headers.get(self.header) == EncodingEnum.DEFLATE

    async def init_decoder(self, headers: MutableHeaders) -> None:
        del headers[self.header]
        self.decompressor = decompressobj()

    def update_decoder(self, data: bytes) -> bytes:
        return self.decompressor.decompress(data)

    def flush_decoder(self) -> bytes:
        return self.decompressor.flush()

    def should_send_with_encoder(self, headers: Headers) -> bool:
        return self.header not in headers

    async def init_encoder(self, headers: MutableHeaders) -> bool:
        headers[DOAXVVHeader(self.header)] = EncodingEnum.DEFLATE
        self.compressor = compressobj(self.compress_level)
        return True

    def update_encoder(self, data: bytes) -> bytes:
        return self.compressor.compress(data)

    def flush_encoder(self) -> bytes:
        return self.compressor.flush()
