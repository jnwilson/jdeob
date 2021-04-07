from Nodes import *


def createProgramNode(node, parent=None):
    p = program.Program(node.type, parent)

    s = createStatementList(node, p)
    
    p.setBody(s)
    
    return p

def createBlockStatement(node, parent):
    block = blockStatement.BlockStatement(node.type, parent)

    statements = createStatementList(node, block)

    block.setBody(statements)

    return block


def createStatementList(node, parent):
    sList = statementList.StatementList("StatementList", parent)

    for statement in node.body:
        s = createStatement(statement, parent)
        sList.addStatement(s)
    
    return sList


def createStatement(node, parent):
    container = statement.Statement("Statement", parent)

    s = createTreeNodes(node, parent)
    container.setStatement(s)

    return container


def createVariableDeclaration(node, parent):
    dec = variableDeclaration.VariableDeclaration(node.type, parent, node.kind)
    for declarator in node.declarations:
        d = createTreeNodes(declarator, dec)
        dec.addDeclaration(d)

    return dec


def createVariableDeclarator(node, parent):
    dec = variableDeclarator.VariableDeclarator(node.type, parent)

    dec.identifier = createTreeNodes(node.id, dec)
    dec.init = createTreeNodes(node.init, dec)

    return dec


def createIdentifier(node, parent):
    i = identifier.Identifier(node.type, parent, node.name)
    return i


def createLiteral(node, parent):
    lit = literal.Literal(node.type, parent, node.value)
    return lit


def createBinaryExpression(node, parent):
    binExpr = binaryExpression.BinaryExpression(node.type, parent)

    binExpr.left = createTreeNodes(node.left, binExpr)
    binExpr.right = createTreeNodes(node.right, binExpr)

    binExpr.operator = createOperator(node.operator, binExpr)

    return binExpr


def createFunctionDeclaration(node, parent):
    func = functionDeclaration.FunctionDeclaration(node.type, parent)
    
    body = createTreeNodes(node.body, func)

    func.setBody(body)

    params = []
    for paramater in node.params:
        p = createStatement(paramater, parent)
        params.append(p)

    func.setParamaters(params)

    return func


def createReturnStatement(node, parent):
    ret = returnStatement.ReturnStatement(node.type, parent)

    arg = createTreeNodes(node.argument, ret)

    ret.setArgument(arg)

    return ret


def createOperator(operator, parent):
    operator_dict = {
        "+": plusOperator.PlusOperator,
        "-": minusOperator.MinusOperator,
        "*": multiplicationOperator.MultiplicationOperator,
        "/": divisionOperator.DivisionOperator,
        "^": exponentOperator.ExponentOperator
    }
    if operator in operator_dict:
        return operator_dict.get(operator)("Operator", parent, operator)
    #else im not sure actually


dispatch = {
    "Program": createProgramNode,
    "VariableDeclaration": createVariableDeclaration,
    "VariableDeclarator": createVariableDeclarator,
    "Identifier": createIdentifier,
    "Literal": createLiteral,
    "BinaryExpression": createBinaryExpression,
    "StatementList": createStatementList,
    "Statement": createStatement,
    "FunctionDeclaration": createFunctionDeclaration,
    "BlockStatement": createBlockStatement,
    "ReturnStatement": createReturnStatement
}


def createTreeNodes(node, parent=None):
    node = dispatch[node.type](node, parent)
    return node
