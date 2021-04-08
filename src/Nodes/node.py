from Nodes import scope


class Node:
    def __init__(self, type, parent):
        self.type = type
        self.parent = parent
        if parent is not None:
            self.scope = parent.scope
        else:
            self.scope = scope.Scope()

    def eval(self, scope):
        return None

    def findConsts(self, consts, variables):
        return None
