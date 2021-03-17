from node import Node

class variableDeclarator(Node):
    def __init__(self, type, parent, id=None, init=None):
        super().__init__(type, parent)
        self.id = id
        self.init = init

    def findConsts(self, consts, variables):
        value = eval(variables)

        if(self.parent.kind == "const"):
            consts.update({id.name: value})

            #{variable name: (value, hasBeenChaned?)}
        if(value is None): #unknown variable value. Can't consider it constant
            variables.update({id.name: (value, True)}) 
        else:
            variables.update({id.name: (value, False)})



