

if __name__ == '__main__':
    f = open("input.txt", "r")
    sum = 0
    while elf_1 := set(f.readline()):
        elf_2 = set(f.readline())
        elf_3 = set(f.readline())
        intersect = elf_1.intersection(elf_2).intersection(elf_3)
        if "\n" in intersect:
            intersect.remove("\n") # Sometimes gets added, no clue why.
        badge = next(iter(intersect))
        if ord(badge) > 96:
            sum += ord(badge) - 96
        else:
            sum += ord(badge) - 65 + 27
    print(sum)
    f.close()
