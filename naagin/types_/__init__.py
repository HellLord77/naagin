from collections.abc import Mapping
from collections.abc import Sequence
from csv import reader
from zlib import compressobj
from zlib import decompressobj

type JSONEncodeType = None | bool | int | float | str | Sequence[JSONEncodeType] | Mapping[str, JSONEncodeType]
type JSONDecodeType = None | bool | int | float | str | list[JSONDecodeType] | dict[str, JSONDecodeType]

CSVReader = type(reader(()))

ZLibCompressor = type(compressobj())
ZLibDecompressor = type(decompressobj())
