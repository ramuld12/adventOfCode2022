import sys

if __name__ == '__main__':
    f = open("Input.txt", "r")
    max_sum = 0
    cur_sum = 0
    while line := f.readline():
        if line.strip() == "":
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum = 0
        else:
            cur_sum += int(line)

    print(max_sum)
