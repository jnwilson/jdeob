import argparse
import subprocess
from src.abstract_syntax_tree import Tree
from src.findConstsDictionary import findConsts

from creator import createTreeNodes


def main():
    #Set up argument parser
    parser = argparse.ArgumentParser(description='A program that deobfuscates JavaScript')

    #required argument. pass the input file directory
    parser.add_argument('input', type=str, help="javascript input file")

    #optional argument. pass a file to output to. if none given outputs to stdout
    parser.add_argument('-o', '--output', dest='output_dir', type=str, help='file to output to')

    #parse arguments. if required arguments are not given, program exits
    args = parser.parse_args()

    #parse code and create the syntax tree (assumes the code is valid)
    with open(args.input, "r", encoding='utf-8') as input_file:
        input_text = input_file.read()

    #tree = Tree(input_text)
    tree = Tree()
    #print(tree.tree)

    program = createTreeNodes(tree.tree)


    consts = {}
    variables = {}

    program.findConsts(consts, variables)

    print(consts)
    print(variables)
    #findConsts(tree.tree.body)

    #convert the python accessible tree to one that the javascript program can manipulate
    js_tree = tree.convert_to_json()

    print("begin dir(json)")

    #cursed but you can use dir(object) for its members, and vars(object) for its values

    level = tree.tree
    print("DIR", dir(level))
    print(vars(level))

    print("end dir(json)")

    def traverse(branch, depth=""):
        flag = True
        try:
            iter(branch)
        except TypeError:
            print(branch.type)
            flag = False
        if flag:
            try:
                print(branch.type)
            except AttributeError:
                pass
            for entry in branch:
                print(depth + "    ", entry.type)
                traverse(entry, depth=depth+"    ")

    #pass the tree over to node.js running astring to generate code from the tree
    #new_source = run_node(js_tree)

    #print tree
    '''
    if args.output_dir:
        output_file = open(args.output_dir, "w")
        output_file.write(new_source)
        output_file.close()
    else:
        print(new_source, end="")
    '''


def run_node(abstract_syntax_tree):
    process = subprocess.Popen(['node', 'main.js', str(abstract_syntax_tree)], stdout=subprocess.PIPE)

    while process.returncode is None:
        process.poll()

    trimmed = str(process.stdout.read())[2: -1].replace("\\n", "\n")
    trailing_newlines = 0
    while len(trimmed) > trailing_newlines + 1 and trimmed[-1 - trailing_newlines] == "\n":
        trailing_newlines += 1
    if trailing_newlines in (0, 1):
        return trimmed
    return trimmed[0:1-trailing_newlines]


def write_to_function(input_str):
    print(input_str)


if __name__ == "__main__":
    main()
