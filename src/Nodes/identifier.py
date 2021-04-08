from Nodes import node


class Identifier(node.Node):
    def __init__(self, type, parent, name):
        super().__init__(type, parent)
        self.name = name
    
    def eval(self):
            return self.scope.getVal(self.name)
            
