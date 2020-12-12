import operator
import typing as t
from construct.core import *

UniOperator = t.Literal[    
    operator.not_,
    operator.neg,
    operator.pos,
]

BinOperator = t.Literal[    
    operator.add,
    operator.sub,
    operator.mul,
    operator.floordiv,
    operator.mod,
    operator.pow,
    operator.xor,
    operator.lshift,
    operator.rshift,
    operator.and_,
    operator.or_,
    operator.contains,
    operator.gt,
    operator.ge,
    operator.lt,
    operator.le,
    operator.eq,
    operator.ne,
]

class ExprMixin(object):
    def __add__(self, other: t.Any) -> BinExpr: ...
    def __sub__(self, other: t.Any) -> BinExpr: ...
    def __mul__(self, other: t.Any) -> BinExpr: ...
    def __floordiv__(self, other: t.Any) -> BinExpr: ...
    def __truediv__(self, other: t.Any) -> BinExpr: ...
    __div__: t.Callable[[t.Any], BinExpr]
    def __mod__(self, other: t.Any) -> BinExpr: ...
    def __pow__(self, other: t.Any) -> BinExpr: ...
    def __xor__(self, other: t.Any) -> BinExpr: ...
    def __rshift__(self, other: t.Any) -> BinExpr: ...
    def __lshift__(self, other: t.Any) -> BinExpr: ...
    def __and__(self, other: t.Any) -> BinExpr: ...
    def __or__(self, other: t.Any) -> BinExpr: ...

    def __radd__(self, other: t.Any) -> BinExpr: ...
    def __rsub__(self, other: t.Any) -> BinExpr: ...
    def __rmul__(self, other: t.Any) -> BinExpr: ...
    def __rfloordiv__(self, other: t.Any) -> BinExpr: ...
    def __rtruediv__(self, other: t.Any) -> BinExpr: ...
    __rdiv__: t.Callable[[t.Any], BinExpr]
    def __rmod__(self, other: t.Any) -> BinExpr: ...
    def __rpow__(self, other: t.Any) -> BinExpr: ...
    def __rxor__(self, other: t.Any) -> BinExpr: ...
    def __rrshift__(self, other: t.Any) -> BinExpr: ...
    def __rlshift__(self, other: t.Any) -> BinExpr: ...
    def __rand__(self, other: t.Any) -> BinExpr: ...
    def __ror__(self, other: t.Any) -> BinExpr: ...

    def __neg__(self) -> UniExpr: ...
    def __pos__(self) -> UniExpr: ...
    def __invert__(self) -> UniExpr: ...
    __inv__: t.Callable[[], UniExpr]

    def __contains__(self, other: t.Any) -> BinExpr: ...
    def __gt__(self, other: t.Any) -> BinExpr: ...
    def __ge__(self, other: t.Any) -> BinExpr: ...
    def __lt__(self, other: t.Any) -> BinExpr: ...
    def __le__(self, other: t.Any) -> BinExpr: ...
    def __eq__(self, other: t.Any) -> BinExpr: ...
    def __ne__(self, other: t.Any) -> BinExpr: ...


class UniExpr(ExprMixin):
    def __init__(self, op: UniOperator, operand: t.Any) -> None: ...
    def __call__(self, obj: Union[Context, dict[str, t.Any]], *args: t.Any) -> t.Any: ...


class BinExpr(ExprMixin):
    def __init__(self, op: BinOperator, lhs: t.Any, rhs: t.Any) -> None: ...
    def __call__(self, obj: Union[Context, dict[str, t.Any]], *args: t.Any) -> t.Any: ...


class Path(ExprMixin):
    def __init__(self, name: str, field: t.Optional[str] = ..., parent: t.Optional[Path] = ...) -> None: ...
    def __call__(self, obj: Union[Context, dict[str, t.Any]], *args: t.Any) -> t.Any: ...
    def __getattr__(self, name: str) -> Path: ...
    def __getitem__(self, name: str) -> Path: ...


class Path2(ExprMixin):
    def __init__(self, name: str, index: t.Optional[int] = ..., parent: t.Optional[Path2] = ...) -> None: ...
    def __call__(self, *args: t.Any) -> t.Any: ...
    def __getitem__(self, index: int) -> Path2: ...


class FuncPath(ExprMixin):
    def __init__(self, func: t.Callable[[t.Any], t.Any], operand: t.Optional[t.Any] = ...) -> None: ...
    def __call__(self, operand: t.Any, *args: t.Any) -> t.Any: ...


this: Path
obj_: Path
list_: Path2

len_: FuncPath
sum_: FuncPath
min_: FuncPath
max_: FuncPath
abs_: FuncPath
