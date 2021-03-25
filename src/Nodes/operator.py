from Nodes import node

class Operator(node.Node):
    def __init__(self, type, parent, operator):
        super().__init__(type, parent)
        self.operator=operator

    def eval(self, left, right, scope):
        return None
