from node import Node

class Literal(Node):
    def __init__(self, type, parent, value=None):
        super().__init__(type, parent)
        self.value = value

    def eval(self, scope):
        return self.value