def get_l_r(lr):
    stack = list(lr)
    while stack:
        l_r = stack.pop(0)
        yield 0 if l_r == "L" else 1
        if not stack:
            stack = list(lr)


def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    lr = str_list.pop(0)
    node_map = {
        line.split(" = ")[0]: (line.split(" (")[1][:3], line[-4:-1])
        for line in str_list
    }
    s = 0
    n = "AAA"
    for l_r in get_l_r(lr):
        n = node_map[n][l_r]
        s += 1
        if n == "ZZZ":
            break
    return s


def get_lcm(list_of_ints):
    from functools import reduce
    from math import gcd

    return reduce(lambda x, y: x * y // gcd(x, y), list_of_ints)


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    lr = str_list.pop(0)
    node_map = {
        line.split(" = ")[0]: (line.split(" (")[1][:3], line[-4:-1])
        for line in str_list
    }

    n_list = [n for n in node_map.keys() if n.endswith("A")]

    list_of_ints = []

    for n in n_list:
        x = 0
        for l_r in get_l_r(lr):
            n = node_map[n][l_r]
            x += 1
            if n.endswith("Z"):
                list_of_ints.append(x)
                break
    return get_lcm(list_of_ints)


if __name__ == "__main__":
    import os

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    custom = open(cur_dir + "/input/08.custom").read()
    test = open(cur_dir + "/input/08.test").read()
    inpt = open(cur_dir + "/input/08").read()
    # print(one(custom))
    # print(one(test))
    # print(one(inpt))
    print(two(custom))
    #print(two(test))
    print(two(inpt))
