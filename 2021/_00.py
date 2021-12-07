from solution import Solution


class Sol(Solution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cleaned(self):
        return [x for x in self.input.split("\n") if x]

    def p1(self):
        return self.cleaned

    def p2(self):
        pass

    @property
    def solution(self):
        return f"p1: {self.p1()}\np2: {self.p2()}\n"


test_ = """
"""

input_ = """
"""


if __name__ == "__main__":
    try:
        Sol(test_).solve()
    except:
        pass
    Sol(input_).solve()
