from Nodes import node


class ReturnStatement(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.argument = None
    
    def setArgument(self, argument):
        self.argument = argument
        
    def eval(self):
        return self.argument.eval()
