import re

from anytree import Node, RenderTree, PostOrderIter

if __name__ == '__main__':
    f = open("input.txt", "r")
    root_dir = Node("/", size=0)
    cur_dir = root_dir
    lines = f.readlines()
    clean_lines = []

    strings = re.findall(r"\n", f.read())
    for line in lines:
        clean_lines.append(line.strip('\n'))
    lines = clean_lines

    for line in lines[1:]:
        if line[0].startswith("$"):  # Command
            command = line[2:]
            if command.startswith("cd"):
                _, dest = command.split(" ")
                if dest == "..":
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = Node(dest, parent=cur_dir, size=0)
                continue
            elif command.startswith("ls"):
                continue

        else:  # Not command, therefore file or directory
            if line.startswith("dir"):
                continue

            else:  # File
                size, name = line.split(" ")
                # name = Node(name, parent=cur_dir, size=size)
                cur_dir.size += int(size)

    for pre, fill, node in RenderTree(root_dir):
        print("%s%s" % (pre, node.name))

    directories = [node for node in PostOrderIter(root_dir, filter_=lambda n: n.parent is not None)]

    result = 0
    for node in directories:
        node.parent.size += int(node.size)
        if int(node.size) <= 100000:
            result += int(node.size)

    print(result)
