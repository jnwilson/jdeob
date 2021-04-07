from Nodes import node, statementList, scope

class Program(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.scope = scope.Scope()
        self.body = statementList.StatementList("StatmentList", self)
        
    def setBody(self, body):
        self.body = body        

    def findConsts(self, consts, variables):
        self.body.findConsts(consts, variables)


