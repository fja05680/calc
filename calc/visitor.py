#from calc import Node

########################################################################
# VISITOR - evaluate the math expression using visitor pattern.
#
# The visitor design pattern is a way of separating an algorithm from
# an object structure on which it operates.
########################################################################

class NodeVisitor:
    def visit(self, node):

        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method:
            return method(node)
        else:
            self.generic_visit(node)

    def generic_visit(self, node):

        raise RuntimeError(f'No method found for node {node}')

class Visitor(NodeVisitor):
    def visit_Plus(self, node):
        return self.visit(node.leftNode) + self.visit(node.rightNode)

    def visit_Minus(self, node):
        return self.visit(node.leftNode) - self.visit(node.rightNode)

    def visit_Multiply(self, node):
        return self.visit(node.leftNode) * self.visit(node.rightNode)

    def visit_Divide(self, node):
        return self.visit(node.leftNode) / self.visit(node.rightNode)

    def visit_Pow(self, node):
        return pow(self.visit(node.leftNode), self.visit(node.rightNode))

    def visit_UPlus(self, node):
        return self.visit(node.operandNode)

    def visit_UMinus(self, node):
        return -self.visit(node.operandNode)

    def visit_Number(self, node):
        return node.value
