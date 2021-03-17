from node import Node

class Program(Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.body = []
    
    def addStatement(self, statement):
        self.body.append(statement)

    def findConsts(self, consts, variables):
        for satement in self.body:
            findConsts(consts, variables)
