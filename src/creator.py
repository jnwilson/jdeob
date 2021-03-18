from Nodes import binaryExpression, identifier, literal, node, program, variableDeclaration, variableDeclarator

def createProgramNode(node, parent=None):
    p = program.Program(node.type, parent)
    for statement in node.body:
        s = createTreeNodes(statement, p)
        p.addStatement(s)
    
    return p

def createVariableDeclaration(node, parent):
    dec = variableDeclaration.VariableDeclaration(node.type, parent, node.kind)
    for declarator in node.declarations:
        d = createTreeNodes(declarator, dec)
        dec.addDeclaration(d)

    return dec

def createVariableDeclarator(node, parent):
    dec = variableDeclarator.VariableDeclarator(node.type, parent)

    dec.ident = createTreeNodes(node.id, dec)
    dec.init = createTreeNodes(node.init, dec)

    return dec

def createIdentifier(node, parent):
    i = identifier.Identifier(node.type, parent, node.name)
    return i

def createLiteral(node, parent):
    lit = literal.Literal(node.type, parent, node.value)
    return lit

def createBinaryExpression(node, parent):
    binExpr = binaryExpression.BinaryExpression(node.type, parent, node.operator)

    binExpr.left = createTreeNodes(node.left, binExpr)
    binExpr.right = createTreeNodes(node.right, binExpr)

    return binExpr



dispatch = {
    "Program" : createProgramNode,
    "VariableDeclaration": createVariableDeclaration,
    "VariableDeclarator" : createVariableDeclarator,
    "Identifier": createIdentifier,
    "Literal": createLiteral,
    "BinaryExpression": createBinaryExpression

}

def createTreeNodes(node, parent=None):
    node = dispatch[node.type](node, parent)
    return node
