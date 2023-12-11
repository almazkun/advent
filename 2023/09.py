def get_next(seq):
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]


def predict_next(seq, last):
    s = get_next(seq)
    last.append(s[-1])
    if all([s[i] == 0 for i in range(len(s))]):
        return s, last
    else:
        return predict_next(s, last)


def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [[int(i) for i in line.split(" ")] for line in str_list]
    s = 0
    for tp in tp_list:
        _, last = predict_next(tp, [])
        s += tp[-1] + sum(last)
    return s


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [[int(i) for i in line.split(" ")] for line in str_list]
    return tp_list


if __name__ == "__main__":
    import os

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    custom = open(cur_dir + "/input/09.custom").read()
    test = open(cur_dir + "/input/09.test").read()
    inpt = open(cur_dir + "/input/09").read()
    print(one(custom))
    print(one(test))
    print(one(inpt))
    print(two(custom))
    print(two(test))
    print(two(inpt))
