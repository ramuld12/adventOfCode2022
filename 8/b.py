import re
import numpy as np

def setup_trees():
    f = open("input.txt", "r")
    lines = f.readlines()
    clean_lines = []
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

def check_one_orientation(height, orientation):
    score = 0
    for tree in orientation:
        if height > tree:
            score += 1
        elif height <= tree:
            score += 1
            return score
        else:
            return score
    return score
def check_scenic_score(x, y, height, trees):
    left  = trees[x, :y]
    right = trees[x, y+1:]
    above = trees[:x, y]
    below = trees[x+1:, y]

    left_score = check_one_orientation(height, reversed(left))
    right_score = check_one_orientation(height, right)
    above_score = check_one_orientation(height, reversed(above))
    below_score = check_one_orientation(height, below)
    return left_score * right_score * above_score * below_score



if __name__ == '__main__':
    trees = setup_trees()
    best_scenic_score = 0

    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees[0]) - 1):
            tree_to_check = trees[x][y]
            cur_scenic_score = check_scenic_score(x, y, tree_to_check, trees)
            if cur_scenic_score > best_scenic_score:
                best_scenic_score = cur_scenic_score

    print(best_scenic_score)




