import numpy as np

# A/X = Rock
# B/Y = Paper
# C/Z = Scissors


if __name__ == '__main__':
    opponent = {
        "A" : 1,
        "B" : 2,
        "C" : 3
    }

    me = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    total_score = 0
    data = np.loadtxt("input.txt", dtype=str)
    for row in range(len(data)):
        o, m = data[row][0], data[row][1]
        if opponent[o] == me[m]:
            total_score += 3
        elif me[m] == (opponent[o] % 3) + 1:
            total_score += 6
        total_score += me[m]
    print(total_score)
