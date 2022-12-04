

if __name__ == '__main__':
    f = open("input.txt", "r")
    sum = 0
    while line := f.readline():
        line_left = slice(0, len(line)//2)
        line_right = slice(len(line)//2, len(line))
        set_left = set(line[line_left])
        set_right = set(line[line_right])
        intersect = set_left.intersection(set_right)
        both = next(iter(intersect))
        if ord(both) > 96:
            sum += ord(both) - 96
        else:
            sum += ord(both) - 65 + 27
    print(sum)
    f.close()
