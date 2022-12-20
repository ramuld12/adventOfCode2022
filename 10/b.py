from util import clean_lines

def find_nr_of_instructions(instructions):
    total = 0
    for line in lines:
        if line.startswith("noop"):
            total += 1
        elif line.startswith("addx"):
            total += 2
    return total

if __name__ == '__main__':
    lines = clean_lines("input.txt")
    nr_inst = find_nr_of_instructions(lines)
    pixels = ["." for i in range(nr_inst)]

    X = 1
    cycle = 0
    for line in lines:

        if line.startswith("noop"):
            cycle += 1
        elif line.startswith("addx"):
            _, to_add = line.split(" ")
            to_add = int(to_add)
            for i in range(2):
                if X - (cycle % 40) in [-1, 0, 1]:
                    pixels[cycle] = "#"
                cycle += 1
            else:
                X += to_add
        if X - (cycle % 40) in [-1, 0, 1]:
            pixels[cycle] = "#"

    for i in range(0, nr_inst, 40):
        print("".join(pixels[i: i + 40]))



