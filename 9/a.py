from util import clean_lines


if __name__ == '__main__':
    lines = clean_lines("input.txt")
    H = [0, 0]
    T = [0, 0]
    visited = set()
    for line in lines:
        direction, moves = line.split(" ")
        for _ in range(int(moves)):
            if direction == "R":
                H[0] += 1
                if T[0] == H[0] - 2:
                    T[0] = H[0] - 1
                    T[1] = H[1]

            elif direction == "L":
                H[0] -= 1
                if T[0] == H[0] + 2:
                    T[0] = H[0] + 1
                    T[1] = H[1]

            elif direction == "U":
                H[1] += 1
                if T[1] == H[1] - 2:
                    T[1] = H[1] - 1
                    T[0] = H[0]

            elif direction == "D":
                H[1] -= 1
                if T[1] == H[1] + 2:
                    T[1] = H[1] + 1
                    T[0] = H[0]
            visited.add((T[0], T[1]))

    print(len(visited))



