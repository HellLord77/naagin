from collections.abc import Mapping
from collections.abc import Sequence

type JSONEncodeType = None | bool | int | float | str | Sequence[JSONEncodeType] | Mapping[str, JSONEncodeType]
type JSONDecodeType = None | bool | int | float | str | list[JSONDecodeType] | dict[str, JSONDecodeType]
