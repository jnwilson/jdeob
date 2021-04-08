from Nodes import node


class StatementList(node.Node):
    def __init__(self, type, parent):
        super().__init__(type, parent)
        self.statementList = []

    def addStatement(self, statement):
        self.statementList.append(statement)

    def findConsts(self, consts, variables):
        for statement in self.statementList:
            statement.findConsts(consts, variables)
