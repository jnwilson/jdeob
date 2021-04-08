class Scope:
    def _init_(self, parent=None, enclosingFunction=None):
        self.parent = parent
        self.enclosingFunction = enclosingFunction
        vars = {}

    def update(self, variable, value):
        self.vars.update({variable: value})
