
def predict_next(seq):
    if all([s==0 for s in seq]):
        return 0
    return seq[-1] + 1 * predict_next([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])

def predict_prev(seq):
    if all([s==0 for s in seq]):
        return 0
    return seq[0] - 1 * predict_prev([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])

def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [[int(i) for i in line.split(" ")] for line in str_list]
    s = 0
    for tp in tp_list:
        s += predict_next(tp)
    return s


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [[int(i) for i in line.split()] for line in str_list]
    s = 0
    for tp in tp_list:
        s += predict_prev(tp)
    return s


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
