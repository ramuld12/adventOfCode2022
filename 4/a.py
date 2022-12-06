

def elf_list_to_set(elf_list):
    elf_set = set()
    for i in range(elf_list[0], elf_list[1] + 1):
        elf_set.add(i)
    return elf_set


if __name__ == '__main__':
    f = open("input.txt", "r")
    sum = 0
    while line := f.readline().strip("\n"):
        elf_left, elf_right = [list(map(int, i.split("-"))) for i in line.split(",")]
        elf_left = elf_list_to_set(elf_left)
        elf_right = elf_list_to_set(elf_right)
        if elf_left.issubset(elf_right) | elf_right.issubset(elf_left):
            sum += 1
    print(sum)
    f.close()
