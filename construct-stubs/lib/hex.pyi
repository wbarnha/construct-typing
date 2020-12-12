import typing as t

class HexDisplayedInteger(int): ...
class HexDisplayedBytes(bytes): ...

K = t.TypeVar("K")
V = t.TypeVar("V")

class HexDisplayedDict(dict[K, V]): ...
class HexDumpDisplayedBytes(bytes): ...
class HexDumpDisplayedDict(dict[K, V]): ...
