from Nodes import node

class BinaryExpression(node.Node):
    def __init__(self, type, parent, operator=None, left=None, right=None):
        super().__init__(type, parent)
        self.operator = operator
        self.left = left
        self.right = right
    
    def eval(self, scope):
        left = self.left.eval(scope)
        right = self.right.eval(scope)

     
        if(left is None or right is None):
            return None

        if(self.operator == "+"):
            return left + right

        if(self.operator == "-"):
            return left - right

        if(self.operator == "*"):
            return left * right

        if(self.operator == "/"):
            return left / right

        return None
    
    
            