import re
from math import ceil

if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()

    stack_nr = ceil(len(lines[0]) // 4)
    stacks = [[] for _ in range(stack_nr)]
    i = 0

    # Create starting stacks
    while (line := lines[i]).find("[") != -1:
        line = line.strip("\n")
        crates = [m.start() for m in re.finditer("\\[", line)]
        for crate in crates:
            curr_stack = crate // 4
            stacks[curr_stack].append(line[crate + 1])
        i += 1

    # Reverse stacks
    i = 0
    for i in range(len(stacks)):
        stacks[i].reverse()

    #
    for j in range(len(lines)):
        curr_line = lines[j]
        if curr_line.find("move") != -1:
            m, f, t = [int(s) for s in re.findall(r'\d+', curr_line)]
            i = 1
            stack_to_move = []
            for i in range(m):
                item = stacks[f - 1].pop()
                stack_to_move.insert(0, item)
            stacks[t - 1].extend(stack_to_move)
    result = ""
    for stack in stacks:
        if len(stack) != 0:
            result += stack.pop()
    print(result)
