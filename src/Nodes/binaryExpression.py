from Nodes import node

class BinaryExpression(node.Node):
    def __init__(self, type, parent, operator=None, left=None, right=None):
        super().__init__(type, parent)
        self.operator = operator
        self.left = left
        self.right = right
    
    def eval(self, scope):
        return self.operator.eval(self.left, self.right, scope)
    
    
            