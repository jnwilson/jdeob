from Nodes import node, blockStatement, scope, valueCreator


class FunctionDeclaration(node.Node):
    def __init__(self, type, parent, name=None):
        super().__init__(type, parent)
        if name is not None:
            parent.scope.update(name, valueCreator.createValue("Function", self))
        self.scope = scope.Scope(parent.scope)
        self.scope.enclosingFunction = self.scope
        self.parameters = []
        self.body = blockStatement.BlockStatement("BlockStatement", self)

    def setBody(self, body):
        self.body = body

    def setParamaters(self, params):
        self.parameters = params

    def findConsts(self, consts, variables):
        #self.scope.print()
        return

    def callEval(self, args):
        #TODO: apply args to function scope

        return None

