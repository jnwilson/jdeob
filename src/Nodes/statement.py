from Nodes import node


class Statement(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.statement = None
        self.isConst = False
        self.value = None

    def setStatement(self, statement):
        self.statement = statement
        
    def findConsts(self, consts, variables):
        self.statement.findConsts(consts, variables)
