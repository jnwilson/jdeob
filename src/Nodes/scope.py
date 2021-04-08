class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.enclosingFunction = self
        if parent is not None:
            self.enclosingFunction = self.parent.enclosingFunction
        
        self.vars = {}

    def update(self, variable, value):
        self.vars[variable] = value

    def getVal(self, name):
        if name in self.vars:
            return self.vars[name].eval()
        elif self.parent is not None:
            return self.parent.getVal(name)

        return None

    def getType(self, name):
        if name in self.vars:
            return self.vars[name].type
        elif self.parent is not None:
            return self.parent.getType(name)

        return None

    def print(self):
        for var in self.vars:
            print(var)
            print(self.vars[var].eval())
        