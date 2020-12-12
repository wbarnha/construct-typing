import typing as t

def int2byte(character: int) -> bytes: ...
def byte2int(character: bytes) -> int: ...
def str2bytes(string: str) -> bytes: ...
def bytes2str(string: bytes) -> str: ...
def iteratebytes(data: bytes) -> t.Iterator[bytes]: ...
def iterateints(data: bytes) -> t.Iterator[int]: ...
def reprstring(data: t.Union[bytes, str]) -> str: ...
def trimstring(data: t.Union[bytes, str]) -> str: ...
def integers2bytes(ints: t.Iterable[int]) -> bytes: ...
def bytes2integers(data: bytes) -> list[int]: ...