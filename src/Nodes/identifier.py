from node import Node

class Identifier(Node):
    def __init__(self, type, parent, name=None):
        super().__init__(type, parent)
        self.name = name
    
    def eval(self, scope):
            return scope[self.name]
            