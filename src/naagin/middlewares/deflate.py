from typing import override
from zlib import Z_DEFAULT_COMPRESSION
from zlib import compressobj
from zlib import decompressobj

from starlette.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp

from naagin.abstract import BaseEncodingMiddleware
from naagin.enums import EncodingEnum
from naagin.types import ZLibCompressor
from naagin.types import ZLibDecompressor
from naagin.utils import CustomHeader

send_header = CustomHeader("Encoding")
receive_header = str(send_header)


class DeflateMiddleware(BaseEncodingMiddleware):
    decompressor: ZLibDecompressor
    compressor: ZLibCompressor

    @override
    def __init__(self, app: ASGIApp, *, send_encoded: bool = True, compress_level: int = Z_DEFAULT_COMPRESSION) -> None:
        super().__init__(app, send_encoded=send_encoded)
        self.compress_level = compress_level

    def should_receive_with_decoder(self, headers: Headers) -> bool:
        return headers.get(receive_header) == EncodingEnum.DEFLATE

    async def init_decoder(self, headers: MutableHeaders) -> None:
        del headers[receive_header]
        self.decompressor = decompressobj()

    def update_decoder(self, data: bytes) -> bytes:
        return self.decompressor.decompress(data)

    def flush_decoder(self) -> bytes:
        return self.decompressor.flush()

    def should_send_with_encoder(self, headers: Headers) -> bool:
        return send_header not in headers

    async def init_encoder(self, headers: MutableHeaders) -> None:
        headers[send_header] = EncodingEnum.DEFLATE
        self.compressor = compressobj(self.compress_level)

    def update_encoder(self, data: bytes) -> bytes:
        return self.compressor.compress(data)

    def flush_encoder(self) -> bytes:
        return self.compressor.flush()
