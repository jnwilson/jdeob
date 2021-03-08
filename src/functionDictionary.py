def evalVariableDeclaration(node):
    if node.kind == "const":
        return True



checkConst = {
    "VariableDeclaration": evalVariableDeclaration
}


