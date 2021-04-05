class Scope:
    def _init_(self, parent=None):
        self.parent = parent
        vars = {}

    def update(self, variable, value):
        self.vars.update({variable: value})
