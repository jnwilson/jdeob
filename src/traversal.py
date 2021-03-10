from src.abstract_syntax_tree import Tree


def not_implemented(node, depth=0):
    print("\t" * depth + "not implemented")


def program(node, depth=0):
    for entry in node.body:
        traverse(entry, depth + 1)


def variable_declaration(node, depth=0):
    for entry in node.declarations:
        traverse(entry, depth + 1)


def variable_declarator(node, depth=0):
    print(node.id)
    print(node.init)


traversal_dictionary = {
    "Program": program,
    "VariableDeclaration": variable_declaration,
    "VariableDeclarator": variable_declarator
}


def traverse(node, depth=0):
    if node.type in traversal_dictionary:
        func = traversal_dictionary.get(node.type)
    else:
        func = not_implemented
    print("\t" * depth + "Type:", node.type)
    func(node, depth)


if __name__ == "__main__":
    tree = Tree()
    #print(tree)
    traverse(tree.tree)
