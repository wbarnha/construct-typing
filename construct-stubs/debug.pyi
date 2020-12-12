import typing as t
from construct.core import Construct, Subconstruct
from construct.core import Context

ContextLambda = t.Callable[[Context], t.Any]

class Probe(Construct[None, None]):
    def __init__(
        self, into: t.Optional[ContextLambda] = ..., lookahead: int = ...
    ) -> None: ...

class Debugger(Subconstruct[None, None]): ...
