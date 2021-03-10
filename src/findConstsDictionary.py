from src.evalDictionary import eval

def evalVariableDeclaration(node, consts):
    if node.kind == "const":
        consts.update({node.declarations[0].id.name: eval(node.declarations[0].init, consts)});
        



dispatch = {
    "VariableDeclaration": evalVariableDeclaration
}


def findConsts(tree):
    listOfConsts={}
    for node in tree:
        dispatch[node.type](node, listOfConsts)

    print(listOfConsts)
    return listOfConsts;



