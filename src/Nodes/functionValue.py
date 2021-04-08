from Nodes import value

class FunctionValue(value.Value):
    def __init__(self, value):
        super().__init__(value)
        self.type = "Function"

    def callEval(self, args):
        return self.value.callEval(args)
