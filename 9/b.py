from util import clean_lines


def move_head(direction, knots):
    match direction:
        case "R":
            knots[0][0] += 1
        case "L":
            knots[0][0] -= 1
        case "U":
            knots[0][1] += 1
        case "D":
            knots[0][1] -= 1
    return knots

def move_other_coordinate(cur_cor, prev_cor):
    if cur_cor < prev_cor:
        cur_cor += 1
    elif cur_cor > prev_cor:
        cur_cor -= 1
    return cur_cor

def move_knots(knots):
    for i in range(1, 10):
        # Previous knot
        prev = knots[i - 1]
        cur = knots[i]
        if cur[0] < prev[0] - 1:
            cur[0] += 1
            cur[1] = move_other_coordinate(cur[1], prev[1])

        elif cur[0] > prev[0] + 1:
            cur[0] -= 1
            cur[1] = move_other_coordinate(cur[1], prev[1])

        if cur[1] < prev[1] - 1:
            cur[1] += 1
            cur[0] = move_other_coordinate(cur[0], prev[0])

        elif cur[1] > prev[1] + 1:
            cur[1] -= 1
            cur[0] = move_other_coordinate(cur[0], prev[0])

        visited.add((knots[9][0], knots[9][1]))
    print(knots)
    return knots

if __name__ == '__main__':
    lines = clean_lines("input.txt")
    knots = [[0, 0] for _ in range(10)]
    visited = set()
    for line in lines:
        direction, moves = line.split(" ")
        for _ in range(int(moves)):
            move_head(direction, knots)
            move_knots(knots)
    print(len(visited))



