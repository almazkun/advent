from _solution import Solution


class _02_Solution(Solution):
    def __init__(self, *args, **kwargs):
        self.horizontal_position = 0
        super().__init__(*args, **kwargs)

    @property
    def cleaned(self):
        return [x for x in self.input.split("\n") if x]

    def p1(self):
        pass

    def p2(self):
        pass

    @property
    def solution(self):
        return p1()


input_ = """
"""


if __name__ == "__main__":
    _02_Solution(input_).solve()
