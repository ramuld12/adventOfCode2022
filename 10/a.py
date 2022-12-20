from util import clean_lines

if __name__ == '__main__':
    lines = clean_lines("input.txt")

    X = 1
    cycle = 1
    sum = 0
    for line in lines:
        if line.startswith("noop"):
            if (cycle % 40) == 20:
                sum += (cycle * X)
                print("Cycle: ", cycle, " X: ", X, " sum: ", sum)

            cycle += 1
        elif line.startswith("addx"):
            _, to_add = line.split(" ")
            to_add = int(to_add)
            for i in range(2):
                if (cycle % 40) == 20:
                    sum += (cycle * X)
                    print("Cycle: ", cycle, " X: ", X, " sum: ", sum)

                cycle += 1
            else:
                X += to_add


    print(sum)




