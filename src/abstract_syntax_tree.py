import esprima


class Tree:
    def __str__(self):
        return str(self.tree)

    def __init__(self, javascript='const x = 10;\nconst y = x * 2 + 1;'):
        #parse code to generate tree
        self.tree = esprima.parse(javascript)

    # reformat from working with python, to working with js
    def convert_to_json(self):
        def character_range(a, b):
            for c in range(ord(a), ord(b) + 1):
                yield chr(c)

        output = ""
        
        abstract_syntax_tree = str(self.tree)
        # replace boolean capitals. rename True to true, and False to false
        abstract_syntax_tree = abstract_syntax_tree.replace(" False", " false")
        abstract_syntax_tree = abstract_syntax_tree.replace(" True", " true")
        # break up the string by line
        for line in abstract_syntax_tree.split("\n"):
            # only lines with colons are invalid
            index_2 = line.find(':')
            if index_2 == -1:
                output += line + "\n"
                continue
            counter = index_2
            index_1 = 0
            # iterate the line backwards until a non letter is found, or there are no more characters
            while counter > 0:
                if line[counter - 1] not in character_range('A', 'z'):
                    index_1 = counter
                    break
                counter -= 1
            # surround each entry with quotation marks to make it a proper json
            output += line[0:index_1] + "\"" + line[index_1:index_2] + "\"" + line[index_2:] + "\n"
        return output


if __name__ == "__main__":
    test = Tree()
    print(test)
