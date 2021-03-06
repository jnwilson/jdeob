from Nodes import node


class Literal(node.Node):
    def __init__(self, type, parent, value=None):
        super().__init__(type, parent)
        self.value = value

    def eval(self):
        return self.value
