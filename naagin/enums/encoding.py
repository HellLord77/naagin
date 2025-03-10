from enum import StrEnum


class EncodingEnum(StrEnum):
    GZIP = "gzip"
    ZLIB = "zlib"
    DEFLATE = "deflate"
