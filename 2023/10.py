class Node:
    def __init__(self, tp, i, j):
        self.tp = tp
        self.i = i
        self.j = j

    @property
    def f_end(self):
        return next_map[self.tp](self.i, self.j)[0]

    @property
    def s_end(self):
        return next_map[self.tp](self.i, self.j)[1]

    def __repr__(self):
        return f"{self.tp}({self.i},{self.j})"


next_map = {
    """
    i,j   0,1   0,2
           N
           ^
           |
    1,0 W <-> E 1,2
           |
           v
           S
    2,0   2,1   2,2     
    
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    """
    "|": lambda i, j: ((i - 1, j), (i + 1, j)),
    "-": lambda i, j: ((i, j - 1), (i, j + 1)),
    "L": lambda i, j: ((i - 1, j), (i, j + 1)),
    "J": lambda i, j: ((i - 1, j), (i, j - 1)),
    "7": lambda i, j: ((i + 1, j), (i, j - 1)),
    "F": lambda i, j: ((i + 1, j), (i, j + 1)),
}


def get_start_node(tp_list):
    for i, row in enumerate(tp_list):
        for j, val in enumerate(row):
            if val == "S":
                return Node(val, i, j)


def get_node_by_coord(i, j, tp_list):
    print(i, j)
    try:
        return Node(tp_list[i][j], i, j)
    except IndexError:
        return None


def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [list(line) for line in str_list]
    node_list = [get_start_node(tp_list)]
    while node_list:
        node = node_list.pop()
        f_end = get_node_by_coord(node.f_end, tp_list)
        s_end = get_node_by_coord(node.s_end, tp_list)
        if f_end and s_end:
            if f_end.tp == "S" or s_end.tp == "S":
                return True
            node_list.append(f_end)
            node_list.append(s_end)

    return node_list


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [list(line) for line in str_list]
    return tp_list


if __name__ == "__main__":
    import os

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    custom = open(cur_dir + "/input/10.custom").read()
    test = open(cur_dir + "/input/10.test").read()
    inpt = open(cur_dir + "/input/10").read()
    print(one(custom))
    print(one(test))
    print(one(inpt))
    # print(two(custom))
    # print(two(test))
    # print(two(inpt))
