import util
def clean_lines(file):
    f = open(file, "r")
    lines = f.readlines()
    clean_lines = []

    for line in lines:
        clean_lines.append(line.strip('\n'))
    return clean_lines