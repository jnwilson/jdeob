from Nodes import node, blockStatement, scope

class FunctionDeclaration(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.scope = scope.Scope(parent.scope)
        self.paramaters = []
        self.body = blockStatement.BlockStatement("BlockStatement", self)

    def setBody(self, body):
        self.body = body

    def setParamaters(self, params):
        self.paramaters = params

    def findConsts(self, consts, variables):
        return self.body.findConsts(consts, variables)
        