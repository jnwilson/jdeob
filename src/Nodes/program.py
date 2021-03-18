from Nodes import node

class Program(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.body = []
    
    def addStatement(self, statement):
        self.body.append(statement)

    def findConsts(self, consts, variables):
        for satement in self.body:
            satement.findConsts(consts, variables)


