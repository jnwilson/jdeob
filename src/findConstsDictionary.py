from src.evalDictionary import eval

def evalVariableDeclaration(node, consts):
    if node.kind == "const":
        value = eval(node.declarations[0].init, consts)
        if (value is None):
            return
        consts.update({node.declarations[0].id.name: value})
        node.declarations[0].init = {"type": "Literal", "value": value, "raw": str(value)}

        
        



dispatch = {
    "VariableDeclaration": evalVariableDeclaration
}


def findConsts(tree):
    listOfConsts={}
    for node in tree:
        dispatch[node.type](node, listOfConsts)

    print(listOfConsts)
    return listOfConsts;



