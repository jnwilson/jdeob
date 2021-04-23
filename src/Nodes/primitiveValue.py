from Nodes import value

class PrimitiveValue(value.Value):
    def __init__(self, value):
        super().__init__(value)
        self.type = "Primitive"
