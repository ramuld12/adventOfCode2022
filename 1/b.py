import sys


def find_calories():
    f = open("input.txt", "r")
    sums = []
    cur_sum = 0
    while line := f.readline():
        if line.strip() == "":
            sums.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(line)

    #Add last line
    sums.append(cur_sum)
    return sums


if __name__ == '__main__':

    # find_calories()
    sums = find_calories()
    sums.sort(reverse=True)
    final_sum = sum(sums[0:3])
    print(final_sum)
