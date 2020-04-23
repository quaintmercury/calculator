

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


class Plus(Expr):

    def __init__(self, left: 'expr', right: 'expr'):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return f"({str(self.left)} + {str(self.right)})"

    def __repr__(self):
        return f"Plus({repr(self.left)}, {repr(self.right)})"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value + right_val.value)
