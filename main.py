import argparse
import esprima
import subprocess


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

    tree = esprima_interface(input_text)
    #print(tree)

    #convert the python accessible tree to one that the javascript program can manipulate
    js_tree = convert_to_json(str(tree))
    #pass the tree over to node.js running astring to generate code from the tree
    new_source = run_node(js_tree)

    if args.output_dir:
        output_file = open(args.output_dir, "w")
        output_file.write(new_source)
        output_file.close()
    else:
        print(new_source, end="")


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


def esprima_interface(program='var help = 5'):
    return esprima.parse(program)


def write_to_function(input_str):
    print(input_str)


#reformat from working with python, to working with js
def convert_to_json(abstract_syntax_tree):
    def character_range(a, b):
        for c in range(ord(a), ord(b) + 1):
            yield chr(c)

    output = ""
    #replace boolean capitals. rename True to true, and False to false
    abstract_syntax_tree = abstract_syntax_tree.replace(" False", " false")
    abstract_syntax_tree = abstract_syntax_tree.replace(" True", " true")
    #break up the string by line
    for line in abstract_syntax_tree.split("\n"):
        #only lines with colons are invalid
        index_2 = line.find(':')
        if index_2 == -1:
            output += line + "\n"
            continue
        counter = index_2
        index_1 = 0
        #iterate the line backwards until a non letter is found, or there are no more characters
        while counter > 0:
            if line[counter - 1] not in character_range('A', 'z'):
                index_1 = counter
                break
            counter -= 1
        #surround each entry with quotation marks to make it a proper json
        output += line[0:index_1] + "\"" + line[index_1:index_2] + "\"" + line[index_2:] + "\n"
    return output


if __name__ == "__main__":
    main()
