def is_digit(line):
    if line[0] in {'s', 'e', 't', 'o', 'n', 'z', 'f'}:
        print(line)
        if line[1] in {'i', 'e', 'o', 'n', 'h', 'w'}:
            print(line)
            if line[2] in {'g', 'e', 'o', 'r', 'n', 'v', 'u', 'x'}:
                print(line)


def parse_line(line):
    for i, char in enumerate(line):
        is_digit(i, char, line)
