import numpy as np


if __name__ == '__main__':
    opponent = {
        "A" : 1,
        "B" : 2,
        "C" : 3
    }

    total_score = 0
    data = np.loadtxt("input.txt", dtype=str)
    for row in range(len(data)):
        o, res = data[row][0], data[row][1]
        if res == 'X':
            total_score += opponent[o] - 1
            if o == 'A':
                total_score += 3
        elif res == 'Y':
            total_score += opponent[o] + 3
        elif res == 'Z':
            total_score += (opponent[o] % 3) + 1 + 6
    print(total_score)
