class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.enclosingFunction = self
        if parent is not None:
            self.enclosingFunction = self.parent.enclosingFunction
        
        self.vars = {}

    def update(self, variable, value):
        self.vars.update({variable: value})
