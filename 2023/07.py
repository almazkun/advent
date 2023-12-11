def compare_card(hand1, hand2):
    card_map = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    if hand1[0] != hand2[0]:
        return card_map[hand1[0]] > card_map[hand2[0]]
    return compare_card(hand1[1:], hand2[1:])


def get_rank(hand):
    """
    comb  r  set
    23456 0  # 5
    22345 1  # 4
    22334 2  # 3
    22234 3  # 3
    22233 4  # 2
    22223 5  # 2
    22222 6  # 1
    """
    hand_set_let = set(hand)
    if len(hand_set_let) == 1:
        return 6
    if len(hand_set_let) == 2:
        for let in hand_set_let:
            if hand.count(let) == 4:
                return 5
        for let in hand_set_let:
            if hand.count(let) == 3:
                return 4
    if len(hand_set_let) == 3:
        is_three = False
        is_two = False
        num_two = 0
        for let in hand_set_let:
            if hand.count(let) == 3:
                is_three = True
            if hand.count(let) == 2:
                is_two = True
        if is_three and is_two:
            return 4
        if is_three:
            return 3
        for let in hand_set_let:
            if hand.count(let) == 2:
                num_two += 1
        if num_two == 2:
            return 2
    if len(hand_set_let) == 4:
        return 1
    return 0


def is_bigger(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    rank_hand1 = get_rank(hand1)
    rank_hand2 = get_rank(hand2)
    if rank_hand1 != rank_hand2:
        return rank_hand1 > rank_hand2
    return compare_card(hand1, hand2)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if is_bigger(x, pivot)]
    right = [x for x in arr[1:] if not is_bigger(x, pivot)]
    return quick_sort(right) + [pivot] + quick_sort(left)


def one(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [
        (tuple(line.split(" ")[0]), int(line.split(" ")[1])) for line in str_list
    ]
    tp_list = quick_sort(tp_list)
    s = 0
    for i, card_bid in enumerate(tp_list):
        s += card_bid[1] * (i + 1)
    return s


def compare_card_two(hand1, hand2):
    card_map = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }
    if hand1[0] != hand2[0]:
        return card_map[hand1[0]] > card_map[hand2[0]]
    return compare_card_two(hand1[1:], hand2[1:])


def j_fication(hand):
    if "J" in hand:
        value_count = {value: hand.count(value) for value in set(hand)}
        value_count = {
            k: v
            for k, v in sorted(
                value_count.items(), key=lambda item: item[1], reverse=True
            )
        }

        for value in value_count.keys():
            if value == "J":
                continue
            else:
                return value


def get_rank_two(hand):
    """
    comb  r  set
    23456 0  # 5
    22345 1  # 4
    22334 2  # 3
    22234 3  # 3
    22233 4  # 2
    22223 5  # 2
    22222 6  # 1
    """
    j_fication_value = j_fication(hand)
    if j_fication_value:
        hand = tuple("".join(hand).replace("J", j_fication_value))
    hand_set_let = set(hand)
    if len(hand_set_let) == 1:
        return 6
    if len(hand_set_let) == 2:
        for let in hand_set_let:
            if hand.count(let) == 4:
                return 5
        for let in hand_set_let:
            if hand.count(let) == 3:
                return 4
    if len(hand_set_let) == 3:
        is_three = False
        is_two = False
        num_two = 0
        for let in hand_set_let:
            if hand.count(let) == 3:
                is_three = True
            if hand.count(let) == 2:
                is_two = True
        if is_three and is_two:
            return 4
        if is_three:
            return 3
        for let in hand_set_let:
            if hand.count(let) == 2:
                num_two += 1
        if num_two == 2:
            return 2
    if len(hand_set_let) == 4:
        return 1
    return 0


def is_bigger_two(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    rank_hand1 = get_rank_two(hand1)
    rank_hand2 = get_rank_two(hand2)
    if rank_hand1 != rank_hand2:
        return rank_hand1 > rank_hand2
    return compare_card_two(hand1, hand2)


def quick_sort_two(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if is_bigger_two(x, pivot)]
    right = [x for x in arr[1:] if not is_bigger_two(x, pivot)]
    return quick_sort_two(right) + [pivot] + quick_sort_two(left)


def two(inpt):
    str_list = [line for line in inpt.split("\n") if line]
    tp_list = [
        (tuple(line.split(" ")[0]), int(line.split(" ")[1])) for line in str_list
    ]
    tp_list = quick_sort_two(tp_list)
    s = 0
    for i, card_bid in enumerate(tp_list):
        s += card_bid[1] * (i + 1)
    return s


if __name__ == "__main__":
    import os

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    custom = open(cur_dir + "/input/07.custom").read()
    test = open(cur_dir + "/input/07.test").read()
    inpt = open(cur_dir + "/input/07").read()
    # print(one(custom))
    print(one(test))
    print(one(inpt))
    # print(two(custom))
    print(two(test))
    print(two(inpt))
