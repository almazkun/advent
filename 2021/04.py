from solution import Solution


class Board:
    def __init__(self, rows_):
        self.rows_ = rows_
        self.draws = []
        self.all = self.rows + self.columns
        self.won = False

    @property
    def rows(self):
        return self.rows_

    @property
    def columns(self):
        return [list(col) for col in zip(*self.rows_)]

    def draw(self, draw):
        self.draws.append(draw)
        win = self.is_win()
        if win:
            score = self.score(draw)
            print(f"#####\t{self} is a win, {draw}, {score}")
            return score

    @property
    def sum_all_unmarked_numbers(self):
        return sum(
            [
                number
                for sublist in self.rows
                for number in sublist
                if number not in self.draws
            ]
        )

    def score(self, draw):
        return self.sum_all_unmarked_numbers * draw

    def is_win(self):
        for row in self.all:
            win = all([elem in self.draws for elem in row])
            if win:
                self.won = True
                return win

    def __repr__(self):
        return f"""
        {self.draws}

        {self.rows[0]}
        {self.rows[1]}
        {self.rows[2]}
        {self.rows[3]}
        {self.rows[4]}\n\n            
        """


class Sol(Solution):
    """--- Day 4: Giant Squid ---
    You're already almost 1.5km (almost a mile) below the surface of the ocean,
    already so deep that you can't see any sunlight. What you can see, however,
    is a giant squid that has attached itself to the outside of your submarine.

    Maybe it wants to play bingo?

    Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
    Numbers are chosen at random, and the chosen number is marked on all boards
    on which it appears. (Numbers may not appear on all boards.) If all numbers
    in any row or any column of a board are marked, that board wins.
    (Diagonals don't count.)

    The submarine has a bingo subsystem to help passengers (currently, you and
    the giant squid) pass the time. It automatically generates a random order
    in which to draw numbers and a random set of boards (your puzzle input).
    For example:

    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
    After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no
    winners, but the boards are marked as follows (shown here adjacent to
    each other to save space):

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    After the next six numbers are drawn (17, 23, 2, 0, 14, and 21),
    there are still no winners:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    Finally, 24 is drawn:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    At this point, the third board wins because it has at least one
    complete row or column of marked numbers (in this case, the entire
    top row is marked: 14 21 17 24 4).

    The score of the winning board can now be calculated. Start by
    finding the sum of all unmarked numbers on that board; in this
    case, the sum is 188. Then, multiply that sum by the number that
    was just called when the board won, 24, to get the final score,
    188 * 24 = 4512.

    To guarantee victory against the giant squid, figure out which
    board will win first. What will your final score be if you
    choose that board?

    --- Part Two ---

    On the other hand, it might be wise to try a different strategy:
    let the giant squid win.

    You aren't sure how many bingo boards a giant squid could play at once,
    so rather than waste time counting its arms, the safe thing to do is to
    figure out which board will win last and choose that one. That way,
    no matter which boards it picks, it will win for sure.

    In the above example, the second board is the last to win, which happens
    after 13 is eventually called and its middle column is completely marked.
    If you were to keep playing until this point, the second board would have a
     sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

    Figure out which board will win last. Once it wins, what would its
    final score be?

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order = None
        self.boards = None
        self.clean()
        self.winners = {}

    def clean(self):
        order, *boards = [x for x in self.input.split("\n\n") if x]
        self.order = [int(x) for x in order.split(",") if x]

        dirty_boards = [x.split("\n") for x in boards if x]
        clean_boards = []
        for dirty_board in dirty_boards:
            clean_board = []
            for dirty_row in dirty_board:
                clean_row = []
                row = [x for x in dirty_row.split(" ") if x]
                for item in row:
                    if item:
                        clean_row.append(int(item))
                if clean_row:
                    clean_board.append(clean_row)
            clean_boards.append(clean_board)
        self.boards = [Board(board) for board in clean_boards]

    def make_draw(self):
        for draw in self.order:
            for board in self.boards:
                score = board.draw(draw)
                if score is not None:
                    return score

    def p1(self):
        pass  # return self.make_draw()

    def p2(self):
        return self.last_to_win()

    def last_to_win(self):
        boards = self.boards.copy()
        draws = self.order.copy()
        while draws:
            draw = draws.pop(0)
            print("+++++", draw, "+++++")
            for board in self.boards:
                if board.won:
                    continue
                else:
                    score = board.draw(draw)
                    print("!!!!!!!boards:", boards)
                    if score is not None:
                        lats_to_win = board, score, draw
                        boards.remove(board)
            if not boards:
                return lats_to_win

    @property
    def solution(self):
        return f"p1: {self.p1()}\np2: {self.p2()}\n"


test_ = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
input_ = """13,47,64,52,60,69,80,85,57,1,2,6,30,81,86,40,27,26,97,77,70,92,43,94,8,78,3,88,93,17,55,49,32,59,51,28,33,41,83,67,11,91,53,36,96,7,34,79,98,72,39,56,31,75,82,62,99,66,29,58,9,50,54,12,45,68,4,46,38,21,24,18,44,48,16,61,19,0,90,35,65,37,73,20,22,89,42,23,15,87,74,10,71,25,14,76,84,5,63,95

88 67 20 19 15
22 76 86 44 73
 7 42  6 69 25
12 68 92 21 75
97 45 13 52 70

75 98 24 18 77
17 93 46 49 13
92 56 97 57 66
44  0 65 54 74
23  6 53 42 20

92 94  9 27 41
73 28 62 90 40
78  3 12 37 32
 8 86 91 16 30
84 38 68 11 19

51  5 12 76 97
72 31 15 61 71
38 32 55 87 10
91  4 85 84 53
59 79 28 69 23

35 48 10 81 60
25 86 24 43 15
44 55 12 54 62
94 89 95  2 23
64 63 45 50 66

80 87 49 88 39
33 81 95 68 55
83 46 36 41 54
90 74  3 52  7
71 40 35  8 77

34 21 24  8 97
99 23 94 70  9
14 98  2 11 10
16 38 92 13 35
82 25 76 42 39

52 76 98 25  3
24 41 13 39 56
11 72 77 47 86
50 32 26 88 48
18 99 22 78 58

22 24 53 84 80
26 97 42 95 11
 1 59 81  7 35
47 14 40 63 30
37 31 10 50 43

26 86 85 69 45
81 43 96 12 42
 7 36  5 28 95
55 90 54  4 46
52 30 79 59 87

76 87 62 13 38
40 44 75  2 37
51 22 58 84 57
 1 29 82 67 35
39 20 31 77 32

53 62 61 26 95
78 44  9  5 97
83 11 18 69  2
94 66  8 14 27
 1  6  7 73 76

87 34 62 93 43
49 20 63 29 22
30 94 11  5 69
74  9 89 41 37
98 38 72 13 97

69 39 15 59 14
42 84 56 23  1
99 16 62 83 89
32 36 33 24  3
22 31 55 10 13

22 44 75  3 17
51 79 37 59 19
98  4 86 35 34
36 20 85  5 23
62 92 43  7 90

 3 68 95 51 71
20 62 47  4 30
60 91 27 86 73
14 76 66 97 85
79 65  8 11 36

38 63  1 64 14
10 52 17 90 98
28 61 29 20 55
49 58 43  3  7
88 81 67 32 68

63 65 15 61 57
47 94  6 14 49
42  3 83 96 31
23 77  1 70 18
45 36 64 48 35

 8 92 88 32 95
26 41 34 11 48
81 35 36 62 28
64 33 52 97 82
 7 37 78  0 86

75 64 84 80 60
17  5 55 95 70
 0 90 68 53 93
 8 50 38  9 65
97 35 26 30  6

76 87 36  5 74
79 94 82 48 20
24 88 90 62 45
 9 40 78 22 68
73 71 35 42 66

52 11 17  9 72
45 13 90  0 80
93 77 37 51 96
 3 68 94 61  1
26 78 12 29 66

49 14 74 11 48
73 58 54  3 40
90 38 62 18 26
53 93 19 41 94
35 63  7 80 68

13 19 92 38  1
63 69  4 99 36
53 57 54 21 80
97 17  2 44 29
 0  3 89 45 58

 9 26 45 57 67
72 10 59 79 88
32  2 87 42 60
62 98  1 93 28
24 99 41 44 29

57 60 54 36 84
28  5 32 66 77
13 19 42 39 37
56 89 74 50 55
 8 71 78  0 80

62 38 24 44  4
17  8 70 77 86
98  6  9 88 23
85 63 78 60 72
71 48 36 69 81

84 19  8 20 17
40 88 33 52 81
29 83 11 36 92
66  6 73 32 82
44 39 26 60 63

13 73 45 32 42
69 20 83  8 84
82 61 11 89 25
 6 92 99 52 57
88 22 46 26 86

74 65 17 64 94
19 34 40 69 80
43 83 45 77 87
41 49 13 51 89
91 72 54  1 60

38 10 16 51 46
80 60 64 62 70
89 71 58 49 39
37  5 35 88 40
93 72 98 42 13

 9 47 91 69 68
27  1 49 60 13
 6 17 95 59 35
26 14 75 57 11
15 18 19 46 74

88 66 25 89  6
63  4 56 73  8
57  0 51  5 36
68 96 84 67 53
49 82  7 32  9

81 75 92  1 62
 0 96 27 63 46
76 31 93 67 12
74 78 59  5 60
69 33 25 94 43

40 72 79 58 22
16 24 99 96 44
69  4 87 90 26
34 43 56 15 35
63 88 89 52 54

43  7 44 31 24
71 18 84 17 64
 8 47 93 85 36
72 29 22 67 74
69 41 58 98 61

55 21 72 14  3
75 12 69 91 54
80 40 78 39  4
44 88 84 76 25
96 57 49 52 28

54 74 32 40 64
 5 94 71 80 22
82 92 79 93 16
53 33 98 85 14
29 49  9 47 12

98 67  8 10  6
58 13 77 99 81
 5 55 21 19  1
 0 26 44 70 93
41 96 31 91 27

50 28 48 13 18
96 43 25  2 78
88 60  0 16 73
12 32 15 68 22
95 74 10 80 21

18 49 85 55 21
11 68 80 59 41
56 94 14 62 60
32 20 40  6  2
42 66 98 71 17

13 38  1 63 82
33 55 54 53 92
36 20 39 84 83
67 43 70 73 75
94 77 76 29 16

82 27 25 18 86
73  3 36 28  1
11 96 40 23 93
58 90 88 35 64
 9 38 69  8 43

87 90 16 56 67
41 75 89  1 80
22 62  5 45 69
28 36 19 96 71
26 63 88 76 31

68 80 83 95 20
75  0 16 38 21
34 89 87 36 14
94 47 53 73 71
63  8 61 96 50

81 23  6 14 26
86 42 82 95 85
77 52 38  2 33
69 98 54 37  4
78 39  3 75 80

92 99 93 28 44
 5  8 67 45 10
61 79 63 85 81
 2 87 76 68 18
69 52 22 16 12

95 50 21 82 60
 5  8  6 28 26
52  3 38 70 74
75  0 53 51 44
10 30 34 47 71

71 44 65 48 51
78 57 75  6 86
95 58 66 12 92
22 61 68 88 50
 4 36 45 28 54

37 17  5  2 52
57 47  4 53 39
11 72 66 81 46
27  0 67 40 83
98 19 10 35 84

43 59 30 72 17
66 50 12 84 65
49 60 14  1 29
89 75 62 82 47
33  5  9 58 45

14  9  3 47 74
69 29 57 62 22
 4 90 40 64 15
21 27 30  2 63
97 96 99 55 41

75 73  3 59 80
65 34 52 20 72
50 84 81 69 41
97 77 19 85 39
88 46 15 35 87

96 42 74 38 78
58 73 67 70 10
62  8 82 64 16
65 25 13  3 89
40 30 53 95 51

 7 16 92 88 38
14 52 46 93 64
49 48  8 76 51
97 67 89 75 19
69  9 29 43 82

81 51 24 57  9
46 43 77 11 35
83  5 14 25 84
70 99 47 37 16
 3 39 75 97 80

18 74 64  6 94
12 59 46 48 31
73 77 33  1 39
 0 69 10 24 56
83 66  5 76 58

40 48 72 65  2
19 28 93 53 44
75 85 42 68 66
99 49 55 31 41
94 35 78 13 61

 4 20 54 33 21
50 61 17 53 64
69 30 24 90 95
82 51 39 52 67
43 73 44 62 83

31 32 63 42 60
39 41 28 51 53
15 20 24 54  5
 9 65 70 57 99
50 29 35  4 47

40 99 95 72 35
10 14 52 83 19
 5 51 87 49 16
60 66 13 63 93
68 57 31  6 78

58 96 49 87 28
95 50 54 53 52
24 16 64  9  5
 7 63  8  4 17
59 98  3 31 25

31 83 61 58 93
94 52 97 30 98
99  2 13 66 73
69 71 68 40 19
74 84 45 25 77

58 85 45 64 74
18 88 91 53  2
93  0 92 55 39
75 49 87 80  4
89 97 57 14 54

20 92 64 50 25
52 90 80 31 38
55 54 10 76 21
95 97  4 77 19
30 26 12 39 11

71 10 84 68 77
48 82 69 75  3
93 24 16 42 60
15 62 76 36 20
21 18 94 22 45

10 91 66 56 75
 6  8 45 59 83
52 93 48 81 87
99 78 43 64 84
21 12 61 71  9

98 77 95 63 15
30 14 39 12 20
13 32 27  0  5
86 80 51 40 99
68 44 26 29 91

92 79 49 44 33
88  4 34  3 90
51 46 31 50 47
61 11 94  6 24
72 18 98 65 57

88 94 93 11 33
75 77 53 54 51
97 15 89 38 76
47 64 55 22  0
40 56 34 19  3

36 55 51 86 91
49 21 78  6 58
90  1 88 45 33
37 69 75 41 50
81 24 34 38 93

21 73 99 50 65
72 77 86  7 68
24 63 71 26 25
 9 12 29 93 87
81 23 22 94 67

37 47 66 89 73
49 23 79 31 86
58 52 21 39 15
60 38 82 50 36
74 30 25 35 99

 6 18 53 36 87
 3 59 50  2 75
69 61 57 19 63
44 77 42 22  7
89 29 45 35 71

28 26 53 47 21
31 71 27 58 85
10 20 74 59 42
89 44 12 91 54
32 87 36 22  7

62 17 61 75 51
44 60 37 14 76
96  0  1 52  5
57 42 97 66 90
12 23 50 98 25

42 30 86 89 66
41 98 39 29 23
75 73 20 79 90
38 60 45 16 18
17 10 47  5 13

 4 10 26 74 38
66 84 60 23 57
30 59 58  2 49
83 82 70 64 43
71 31 35 90  0

27 99 33 56  3
41 97  1 68 88
43 63 81 89 22
30 32 59 64 12
84 58 10 39 76

98 16 75 27 57
 0  9  3 79 50
 5 34 93  6 21
52 70 87 31 49
58 46 24 20 45

78 24 19 13 30
83 59 79 37 72
84 81 99 17 77
10 93  3 33 70
29 35 49  6  5

47  6 82 94 53
83 19 25 54 64
 9 56 39 31 96
 1 81 66 41  5
55 48 43 12 14

47 55 86 31 17
89 45 65 34 56
99 88 18 97  3
52 21 14 68 13
 9 26 22  7 32

75 27 62 19 72
20 49  7 21 85
53 46  1 59 99
61 71 87 24 83
 5 77 41 51 73

57 59 82 77 52
99 49 81 37 54
70 89 23 20 90
31  1 21 98 66
86 35 46 36 18

37 39 70 76 27
68 84 25  1 33
50 82 77 20 44
18 11 51 62 54
80 67 35 89 30

85 96  1  3 73
25 47 10 46 98
 2 33 91 71 35
 0 32 11 55 67
14 81 17  5 94

68 84 46 43 81
42 35 48 89 30
 4 17 65 77  6
49 97 85 12 66
75 25 13 90 51

94 42 46 58 56
97 50 86 84 15
52  9 28 32 59
26 96 91 57 83
29 99 18 31 43

 2 19 31 10 32
81 16 50 59  7
76 30 63 44 95
82 54 61 75 36
85 78 12 67  9

92  1 72 27 37
22 13 91  4 34
53 82 76 70 19
99 38 59 33 52
 0 61 36 67 75

94 41  5 57  1
37 36 99 34 47
40 93 62 32 76
61 75 48 42 73
35 69 54 13 50

76 12 51 11 74
30 83 73 33 78
95 77 15 14 80
86 37 91 50 10
52 67  3 60 17

68  7 42 81 15
46 58  9 31 18
91  1 28 34 37
17 57  6  2 70
97 54 20 27 44

44 80 45 28 14
94 47 29 50 54
64 67 96 95 93
76 36 82 39 43
30 55 97  3  2

43  2 15 99 34
97 75 26  9 67
30 63 74 12 82
18  6 49 48 55
47 36 41 56 83

26 70 87 80 89
17 50 61 21 96
43 83 85 46 64
66 75 23 47 69
22 72 55 52  8

67 54 11 29 42
16 45 56 86 66
 4 80 43 72 91
90 87 63 39 50
32  6 59 27 89

14 92 78 47 59
98  0 63 85 31
52  8 84 70 91
43  3 76 65 57
87 22 99 94 58

26 53 58 52  1
82 57 32 40 20
72 21 74 46 43
41 15 98  2 11
 5 96 22 18 55"""


if __name__ == "__main__":
    try:
        Sol(test_).solve()
    except:
        pass
    Sol(input_).solve()
