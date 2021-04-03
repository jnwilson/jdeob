from abstract_syntax_tree import Tree

#cases for expressions that should be evaluated/simplified
#should probably use node to evaluate them or custom functions

test_one = [
    "let x = 1 + 1",
    "let x = 2"]

test_two = [
    "let x = 5\nlet y = x + 1",
    "let x = 5\nlet y = 6"]

test_three = [
    "let x = true ? 1 : 2",
    "let x = 1"]

test_four = [
    "let x = 3 * 2",
    "let x = 6"
]


def evaluate(value_left, operator, value_right):
    if eval(str(value_left) + operator + str(value_right)):
        return eval(str(value_left) + operator + str(value_right))
    else:
        return "error"


def lookup(variable_name):
    #I guess have a way to reference other values
    return -1


def evaluate_expression(left, operator, right):
    def get_value(node):
        if node.type == "Identifier":
            return lookup(node.name)
        if node.type == "BinaryExpression":
            return evaluate_expression(node.left, node.operator, node.right)
        if node.type == "Literal":
            return node.value

    left_value = get_value(left)
    right_value = get_value(right)

    return eval(str(left_value) + operator + str(right_value))


def evaluate(node):  # takes VariableDeclarator node
    if node.init.type == "Literal":
        #no need to evaluate
        return node.init.value
    if node.init.type == "BinaryExpression":
        return evaluate_expression(node.init.left, node.init.operator, node.init.right)


if __name__ == "__main__":
    tree = Tree("let x = 1 + 1 * 1")
    #print(tree.tree)
    print("this evaluates to", evaluate(tree.tree.body[0].declarations[0]))

