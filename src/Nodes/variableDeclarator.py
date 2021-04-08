from Nodes import node, valueCreator


class VariableDeclarator(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.identifier = None
        self.init = None

    def setIdentifier(self, ident):
        self.identifier = ident
        self.scope.update(ident.name, valueCreator.createValue("Undefined", None))

    def setInit(self, value):
        self.init = value
        
        if value.type == "Identifier":
            self.scope.update(self.identifier.name, valueCreator.createValue(self.scope.getType(value.name), value.eval()))
        elif value.type == "FunctionExpression":
            self.scope.update(self.identifier.name, valueCreator.createValue("Function", value.eval()))
        else:
            self.scope.update(self.identifier.name, valueCreator.createValue("Primitive", value.eval()))



    def findConsts(self, consts, variables):
        value = self.init.eval()

        if self.parent.kind == "const":
            consts.update({self.identifier.name: value})

        #{variable name: (value, hasBeenChanged?)}
        if value is None:  # unknown variable value. Can't consider it constant
            variables.update({self.identifier.name: self.scope.getVal(self.identifier.name)}) 
        else:
            variables.update({self.identifier.name: self.scope.getVal(self.identifier.name)})
