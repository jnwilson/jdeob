def evalLiteral(tree, scope):
    return tree.value;

def evalBinaryExpr(tree, scope):
    if(tree.operator == "+"):
        return eval(tree.left, scope) + eval(tree.right, scope);

    if(tree.operator == "-"):
        return eval(tree.left, scope) - eval(tree.right, scope);

    if(tree.operator == "*"):
        return eval(tree.left, scope) * eval(tree.right, scope);

    if(tree.operator == "/"):
        return eval(tree.left, scope) / eval(tree.right, scope);    

def evalIdentifier(tree, scope):
    return scope[tree.name];

dispatch = {
    "Literal": evalLiteral,
    "BinaryExpression": evalBinaryExpr,
    "Identifier": evalIdentifier
}

def eval(tree, scope):
    return dispatch[tree.type](tree, scope)