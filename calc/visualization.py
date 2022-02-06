import pydot

########################################################################
# Visualization - use graphviz for visualization of the syntax tree.
########################################################################

class NodeVisitor:
    def visit(self, node, parent_node_num=0):

        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method:
            return method(node, parent_node_num)
        else:
            self.generic_visit(node)

    def generic_visit(self, node):

        raise RuntimeError(f'No method found for node {node}')


class Visualization(NodeVisitor):
    def __init__(self):
        self.graph = pydot.Dot(graph_type='graph')
        self.node_num = 0

    def _graph_node_edge(self, label, parent_node_num):
        self.node_num += 1
        node_num = self.node_num
        self.graph.add_node(pydot.Node(str(node_num), label=label, shape='circle'))
        if parent_node_num > 0:
            self.graph.add_edge(pydot.Edge(str(parent_node_num), str(node_num)))
        return node_num

    def visit_Plus(self, node, parent_node_num):
        node_num = self._graph_node_edge('+', parent_node_num)
        self.visit(node.leftNode, node_num); self.visit(node.rightNode, node_num)

    def visit_Minus(self, node, parent_node_num):
        node_num = self._graph_node_edge('-', parent_node_num)
        self.visit(node.leftNode, node_num); self.visit(node.rightNode, node_num)

    def visit_Multiply(self, node, parent_node_num):
        node_num = self._graph_node_edge('*', parent_node_num)
        self.visit(node.leftNode, node_num); self.visit(node.rightNode, node_num)

    def visit_Divide(self, node, parent_node_num):
        node_num = self._graph_node_edge('/', parent_node_num)
        self.visit(node.leftNode, node_num); self.visit(node.rightNode, node_num)

    def visit_Pow(self, node, parent_node_num):
        node_num = self._graph_node_edge('**', parent_node_num)
        self.visit(node.leftNode, node_num); self.visit(node.rightNode, node_num)

    def visit_UPlus(self, node, parent_node_num):
        node_num = self._graph_node_edge('+', parent_node_num)
        self.visit(node.operandNode, node_num)

    def visit_UMinus(self, node, parent_node_num):
        node_num = self._graph_node_edge('-', parent_node_num)
        self.visit(node.operandNode, node_num)

    def visit_Number(self, node, parent_node_num):
        node_num = self._graph_node_edge(str(node.value), parent_node_num)

    def write_png(self, filename='output.png'):
        self.graph.write_png(filename)
