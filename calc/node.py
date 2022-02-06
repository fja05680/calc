########################################################################
# NODE
#
# Create a data structure which can represent math expressions that
# supports the following:
#   * Real numbers
#   * plus(+)
#   * minus(-)
#   * multiply(*)
#   * divide(/)
#   * pow(**)
#   * parenthesis
#   * implicit multiplication, i.e. 3(2) is 3*2
#
# Implement an evaluation method which calculates the value of
# the expression.
#
# Implement a `__str__` method which converts the data structure into
# an ascii string equivalent.
########################################################################

class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def evaluate(self):
        return self.value


class BinOp(Node):
    def __init__(self, leftNode, rightNode):
        self.leftNode = leftNode
        self.rightNode = rightNode


class UnaryOp(Node):
    def __init__(self, operandNode):
        self.operandNode = operandNode


class Plus(BinOp):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode)

    def __str__(self):
        return f'({self.leftNode}+{self.rightNode})'

    def evaluate(self):
        return self.leftNode.evaluate() + self.rightNode.evaluate()


class Minus(BinOp):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode)

    def __str__(self):
        return f'({self.leftNode}-{self.rightNode})'

    def evaluate(self):
        return self.leftNode.evaluate() - self.rightNode.evaluate()


class Multiply(BinOp):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode)

    def __str__(self):
        return f'{self.leftNode}*{self.rightNode}'

    def evaluate(self):
        return self.leftNode.evaluate() * self.rightNode.evaluate()


class Divide(BinOp):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode)

    def __str__(self):
        return f'{self.leftNode}/{self.rightNode}'

    def evaluate(self):
        return self.leftNode.evaluate() / self.rightNode.evaluate()


class Pow(BinOp):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode)

    def __str__(self):
        return f'{self.leftNode}**{self.rightNode}'

    def evaluate(self):
        return pow(self.leftNode.evaluate(), self.rightNode.evaluate())


class UPlus(UnaryOp):
    def __init__(self, operandNode):
        super().__init__(operandNode)

    def __str__(self):
        return f'+{self.operandNode}'

    def evaluate(self):
        return self.operandNode.evaluate()


class UMinus(UnaryOp):
    def __init__(self, operandNode):
        super().__init__(operandNode)

    def __str__(self):
        return f'-{self.operandNode}'

    def evaluate(self):
        return -1 * self.operandNode.evaluate()

