from solution import Solution


class Sol(Solution):
    """--- Day 7: The Treachery of Whales ---

    A giant whale has decided your submarine is its next meal,
    and it's much faster than you are. There's nowhere to run!

    Suddenly, a swarm of crabs (each in its own tiny submarine
    - it's too deep for them otherwise) zooms in to rescue you!
    They seem to be preparing to blast a hole in the ocean floor;
    sensors indicate a massive underground cave system just
    beyond where they're aiming!

    The crab submarines all need to be aligned before they'll
    have enough power to blast a large enough hole for your
    submarine to get through. However, it doesn't look like
    they'll be aligned before the whale catches you! Maybe
    you can help?

    There's one major catch - crab submarines can only move
    horizontally.

    You quickly make a list of the horizontal position of
    each crab (your puzzle input). Crab submarines have limited fuel,
    so you need to find a way to make all of their horizontal
    positions match while requiring them to spend as little fuel
    as possible.

    For example, consider the following horizontal positions:

    16,1,2,0,4,2,7,1,2,14
    This means there's a crab with horizontal position 16, a
    crab with horizontal position 1, and so on.

    Each change of 1 step in horizontal position of a single
    crab costs 1 fuel. You could choose any horizontal
    position to align them all on, but the one that costs the
    least fuel is horizontal position 2:

    Move from 16 to 2: 14 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 0 to 2: 2 fuel
    Move from 4 to 2: 2 fuel
    Move from 2 to 2: 0 fuel
    Move from 7 to 2: 5 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 14 to 2: 12 fuel
    This costs a total of 37 fuel.
    This is the cheapest possible outcome;
    more expensive outcomes include aligning
    at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

    Determine the horizontal position that the crabs can align
    to using the least fuel possible. How much fuel must they
    spend to align to that position?
    --- Part Two ---

    The crabs don't seem interested in your
    proposed solution.
    Perhaps you misunderstand crab engineering?

    As it turns out, crab submarine engines
    don't burn fuel at a constant rate.
    Instead, each change of 1 step in horizontal
    position costs 1 more unit of fuel than the last:
    the first step costs 1, the second step costs 2,
    the third step costs 3, and so on.

    As each crab moves, moving further
    becomes more expensive.
    This changes the best horizontal position
    to align them all on; in the example above,
    this becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel
    This costs a total of 168 fuel.
    This is the new cheapest possible outcome;
    the old alignment position (2) now costs 206 fuel instead.

    Determine the horizontal position that the crabs can
    align to using the least fuel possible so they
    can make you an escape route! How much fuel
    must they spend to align to that position?
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cleaned(self):
        return [int(x) for x in self.input.split(",") if x]

    def p1(self):
        def sum_of_diffs(lst, delta):
            sum_ = 0
            for position in self.cleaned:
                sum_ += abs(position - delta)
            return sum_

        def get_delta(lst):
            return min(lst, key=lambda x: sum_of_diffs(lst, x))

        delta = get_delta(self.cleaned)

        return sum_of_diffs(self.cleaned, delta)

    def p2(self):
        def fuel_for_delta(delta):
            return sum([i + 1 for i in range(delta)])

        most_min = float("inf")
        for i in range(min(self.cleaned), max(self.cleaned) + 1):
            sum_ = 0
            for position in self.cleaned:
                sum_ += fuel_for_delta(abs(position - i))
            if sum_ < most_min:
                most_min = sum_
        return most_min

    @property
    def solution(self):
        return f"p1: {self.p1()}\np2: {self.p2()}\n"


test_ = """16,1,2,0,4,2,7,1,2,14"""

input_ = """1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,62,461,1087,183,1096,431,412,200,486,1543,25,580,1030,15,65,1186,9,226,173,77,119,691,855,451,88,741,221,1465,190,779,327,179,627,366,288,174,1147,49,773,3,5,65,20,172,601,307,611,699,1168,933,1295,832,242,62,8,4,226,768,33,566,21,10,937,15,760,100,574,181,89,72,1054,225,28,0,685,661,131,281,933,90,233,109,1345,81,106,636,1262,193,172,1056,709,1176,447,536,1054,929,171,226,127,274,710,917,218,192,25,128,321,1816,515,181,759,20,258,134,281,151,99,479,623,534,72,576,534,337,54,293,450,230,963,14,357,446,1244,964,16,865,52,1,1171,77,7,275,313,894,577,305,1119,393,285,354,136,1147,241,441,166,1024,650,101,178,1514,186,902,367,5,431,374,56,507,857,1316,0,186,63,118,1062,62,446,266,47,354,168,65,1036,447,689,160,749,728,791,1066,99,675,194,891,153,737,801,254,905,1046,21,413,386,204,603,373,218,440,137,1340,1616,121,903,722,841,731,213,219,405,336,1345,144,329,285,213,272,717,47,126,1137,548,32,21,755,219,595,187,143,636,476,397,185,70,345,89,319,80,867,26,1166,509,24,16,151,605,1415,893,814,473,289,377,407,44,184,290,447,1669,116,319,455,294,145,513,58,247,186,1565,31,297,1,226,1051,1561,1233,254,1274,422,547,1638,354,1855,419,71,1003,626,519,109,96,996,117,32,226,424,184,181,720,1311,1162,11,86,438,408,1269,887,612,327,133,1117,1390,345,10,370,175,37,1154,659,707,193,665,65,359,758,1253,498,219,601,59,919,1371,289,9,437,392,626,981,2,51,733,780,101,541,770,464,28,616,81,1708,1515,719,780,1214,673,268,246,25,252,301,205,27,160,0,298,69,285,58,809,1369,812,628,353,47,632,123,168,135,277,303,614,365,330,1385,1117,1346,737,744,1403,385,215,437,276,726,673,668,494,164,1,763,696,487,252,375,1253,42,1111,963,58,63,11,1648,1080,964,526,454,1349,1098,95,59,78,36,42,654,1441,1129,464,740,355,370,44,4,154,986,439,828,287,969,765,565,836,196,387,556,34,586,438,1205,760,798,6,61,260,25,418,1628,566,3,530,753,758,16,92,30,1388,109,240,513,1048,1056,588,1634,418,297,195,447,1145,198,466,0,607,180,57,58,72,319,221,869,744,339,195,1295,268,1336,1310,38,714,326,393,445,422,102,389,188,147,21,805,381,520,561,282,438,115,431,156,482,50,890,470,22,60,46,1588,971,1219,82,380,1061,948,455,99,255,400,1832,91,225,280,520,279,91,172,92,946,434,182,164,142,83,91,281,538,962,77,1104,1522,310,4,961,62,9,1257,596,464,733,338,1166,334,380,509,773,90,498,480,1523,1632,530,543,413,589,748,4,861,11,233,192,699,33,615,1853,205,270,624,1132,1100,227,1402,349,183,179,645,4,1120,962,317,326,128,422,281,302,701,53,179,34,802,272,1254,375,764,418,16,160,943,479,416,717,644,1029,372,140,114,449,351,159,305,1299,749,488,502,180,210,17,533,258,120,333,1097,185,1911,451,360,66,1329,1260,209,1611,454,809,336,783,1438,20,26,609,720,155,578,367,231,1715,64,610,465,752,81,108,389,995,244,1291,1144,159,161,1630,561,813,261,67,1604,124,231,833,14,15,1245,1309,1165,103,1270,228,1,133,644,581,218,481,716,237,155,360,110,1408,931,99,216,5,21,67,348,927,325,759,1127,557,584,696,428,653,548,247,1519,1682,132,3,1648,230,229,136,253,543,1153,204,669,58,81,357,85,82,749,503,139,32,1170,1352,151,653,1441,51,392,474,2,114,64,418,125,514,838,473,794,331,13,327,1476,836,37,3,0,115,18,1784,300,190,99,997,1164,31,1255,96,64,1101,354,698,372,852,1508,100,289,32,704,292,504,191,1342,231,692,12,369,1182,62,809,566,688,218,2,539,234,996,444,228,456,369,115,23,29,226,940,95,404,349,1254,171,69,711,2,1405,1181,34,8,92,173,533,20,181,921,201,1236,185,457,526,2,106,12,601,58,339,457,590,15,1583,473,451,1124,1569,401,72,154,9,1331,471,165,516,463,543,298,197,43,1294,101,1058,1025,1099,4,634,90,104,870,480,412,290,11,924,338,30,281,83,268,20,848,1722,1060,987,9,196,266,28,402,267,199,814,986,440,906,796,1403,1394,62,136,442,412,1729,571,459,91,730,269,172,202,772,305"""


if __name__ == "__main__":
    try:
        Sol(test_).solve()
    except:
        pass
    Sol(input_).solve()
