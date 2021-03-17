from node import Node 

class VariableDeclaration(Node):
    def __init__(self, type, parent, kind):
        super().__init__(type, parent)
        self.kind = kind
        self.declarations = []
    
    def addDeclaration(self, declarator):
        self.declarations.append(declarator)

    def findConsts(self, consts, variables):
        for dec in self.declarations:
            dec.findConsts(consts, variables)
    

