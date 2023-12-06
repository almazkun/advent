def get_distance(time, limit):
    return [
        (time - i) * (i * 1) for i in range(0, time) if (time - i) * (i * 1) > limit
    ]


def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    time_list = [int(c) for c in str_list[0].split(":")[1].split()]
    distance_list = [int(c) for c in str_list[1].split(":")[1].split()]
    s = 1
    for i, time in enumerate(time_list):
        s *= len(get_distance(time, distance_list[i]))
    return s


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    time_list = [int((str_list[0].split(":")[1]).replace(" ", ""))]
    distance_list = [int((str_list[1].split(":")[1]).replace(" ", ""))]
    s = 1
    for i, time in enumerate(time_list):
        s *= len(get_distance(time, distance_list[i]))
    return s


if __name__ == "__main__":
    test = """Time:      7  15   30
Distance:  9  40  200"""
    inpt = """Time:        40     82     84     92
Distance:   233   1011   1110   1487"""
    print(one(test))
    print(one(inpt))
    print(two(test))
    print(two(inpt))
