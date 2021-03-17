class Node:
    def __init__(self, type, parent):
        self.type = type
        self.parent = parent

    def eval(self, scope):
        return None

    def findConsts(self, consts, variables):
        return None

    