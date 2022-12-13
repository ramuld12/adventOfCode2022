import re
import numpy as np

def setup_trees():
    f = open("input.txt", "r")
    lines = f.readlines()
    clean_lines = []

    strings = re.findall(r"\n", f.read())
    for line in lines:
        clean_lines.append(line.strip('\n'))
    lines = clean_lines

    trees = np.zeros(dtype=int, shape=(len(lines[0]), len(lines[0])))
    i = 0
    for line in lines:
        for j in range(len(line)):
            trees[i][j] = line[j]
        i += 1
    return trees

def check_visibility(x, y, height, trees):
    left  = trees[x, :y]
    right = trees[x, y+1:]
    above = trees[:x, y]
    below = trees[x+1:, y]

    if all(height > i for i in left) | all(height > i for i in right) | all(height > i for i in above) | all(height > i for i in below):
        return True
    return False

if __name__ == '__main__':
    trees = setup_trees()
    sum = (len(trees[0]) * 4) - 4

    # Counter start/count outer rim
    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees[0]) - 1):
            tree_to_check = trees[x][y]
            if check_visibility(x, y, tree_to_check, trees):
                sum += 1

    print(sum)




