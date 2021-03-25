from Nodes import operator

class PlusOperator(operator.Operator):
    def __init__(self, type, parent, operator):
        super().__init__(type, parent, operator)
        self.operator=operator

    def eval(self, left, right, scope):
        l = left.eval(scope)
        r = right.eval(scope)

        if(left is None or right is None):
            return None

        return l + r
