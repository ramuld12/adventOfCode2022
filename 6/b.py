
if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()

    buffer = []
    for x in range(14):
        buffer.append(lines[0][x])

    for i in range(14, len(lines[0])):
        del buffer[0]
        buffer.append(lines[0][i])
        buffer_set = set(buffer)
        if (len(buffer) == len(buffer_set)) & (len(buffer_set) == 14):
            print(i + 1)
            break
        i += 1
