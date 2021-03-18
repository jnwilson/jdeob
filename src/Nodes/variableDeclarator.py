from Nodes import node

class VariableDeclarator(node.Node):
    def __init__(self, type, parent, ident=None, init=None):
        super().__init__(type, parent)
        self.ident = ident
        self.init = init

    def findConsts(self, consts, variables):
        value = self.init.eval(variables)

        if(self.parent.kind == "const"):
            consts.update({self.ident.name: value})
            

            #{variable name: (value, hasBeenChaned?)}
        if(value is None): #unknown variable value. Can't consider it constant
            variables.update({self.ident.name: (value, True)}) 
        else:
            variables.update({self.ident.name: (value, False)})



