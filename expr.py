

class Expr(object):
    """Abstract base class of all expressions."""

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError("Each concrete Expr class must define 'eval'")

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        raise NotImplementedError("Each concrete Expr class must define __str__")

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        raise NotImplementedError("Each concrete Expr class must define __repr__")


class IntConst(Expr):

    def __init__(self, value: 'int'):
        self.value = value

    def __eq__(self, other: 'Expr'):
        return isinstance(other, IntConst) and self.value == other.value

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self

    def __repr__(self):
        return f"IntConst({self.value})"


class Plus(BinOp):
    """Expr + Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, "+", "Plus")

    def __repr__(self):
        return f"Plus({repr(self.left)}, {repr(self.right)})"


    def _apply(self, left: int, right: int) -> int:
        return left + right


class Times(BinOp):
    """left * right"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, "*", "Times")

    def _apply(self, left: int, right: int):
        return left * right

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return f"Times({repr(self.left)}, {repr(self.right)})"


class BinOp(Expr):

    def __init__(self):
        raise NotImplementedError("Do not instantiate BinOp")

    def _binop_init(self, left: Expr, right: Expr, op_sym: str, op_name: str):
        self.left = left
        self.right = right
        self.op_sym = op_sym
        self.op_name = op_name

    def __str__(self) -> str:
        return f"({self.left} {self.op_sym} {self.right})"

    def __repr__(self) -> str:
        return f"{self.op_name}({repr(self.left)}, {repr(self.right)})"

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(self._apply(left_val.value, right_val.value))
