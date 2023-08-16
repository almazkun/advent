def main():
    stacks = [[] for _ in range(9)]
    """
    [N] [G]                     [Q]    
    [H] [B]         [B] [R]     [H]    
    [S] [N]     [Q] [M] [T]     [Z]    
    [J] [T]     [R] [V] [H]     [R] [S]
    [F] [Q]     [W] [T] [V] [J] [V] [M]
    [W] [P] [V] [S] [F] [B] [Q] [J] [H]
    [T] [R] [Q] [B] [D] [D] [B] [N] [N]
    [D] [H] [L] [N] [N] [M] [D] [D] [B]
     1   2   3   4   5   6   7   8   9 
    """
    stacks[0] = ["D", "T", "W", "F", "J", "S", "H", "N"]
    stacks[1] = ["H", "R", "P", "Q", "T", "N", "B", "G"]
    stacks[2] = [
        "L",
        "Q",
        "V",
    ]
    stacks[3] = ["N", "B", "S", "W", "R", "Q"]
    stacks[4] = ["N", "D", "F", "T", "V", "M", "B"]
    stacks[5] = ["M", "D", "B", "V", "H", "T", "R"]
    stacks[6] = ["D", "B", "Q", "J"]
    stacks[7] = ["D", "N", "J", "V", "R", "Z", "H", "Q"]
    stacks[8] = ["B", "N", "H", "M", "S"]

    commands = """move 3 from 1 to 2
move 1 from 7 to 1
move 1 from 6 to 5
move 5 from 5 to 9
move 2 from 5 to 2
move 1 from 6 to 8
move 1 from 5 to 7
move 5 from 4 to 6
move 1 from 7 to 6
move 1 from 2 to 4
move 5 from 2 to 6
move 2 from 1 to 5
move 2 from 1 to 9
move 16 from 6 to 4
move 6 from 8 to 3
move 7 from 2 to 4
move 5 from 9 to 3
move 1 from 1 to 4
move 1 from 1 to 3
move 3 from 7 to 4
move 2 from 5 to 4
move 31 from 4 to 8
move 22 from 8 to 4
move 9 from 3 to 6
move 7 from 9 to 5
move 4 from 5 to 6
move 6 from 3 to 2
move 2 from 6 to 7
move 5 from 2 to 7
move 1 from 2 to 4
move 1 from 7 to 5
move 4 from 5 to 4
move 2 from 6 to 9
move 2 from 4 to 6
move 7 from 6 to 4
move 2 from 6 to 1
move 1 from 6 to 8
move 8 from 8 to 1
move 1 from 7 to 6
move 4 from 1 to 5
move 9 from 4 to 8
move 4 from 1 to 7
move 3 from 5 to 3
move 2 from 1 to 9
move 1 from 3 to 2
move 1 from 9 to 8
move 1 from 2 to 1
move 1 from 1 to 8
move 1 from 5 to 1
move 2 from 3 to 1
move 2 from 6 to 9
move 19 from 4 to 1
move 4 from 4 to 2
move 6 from 1 to 4
move 1 from 2 to 4
move 4 from 4 to 3
move 7 from 7 to 3
move 7 from 8 to 2
move 2 from 7 to 4
move 3 from 2 to 1
move 8 from 8 to 2
move 3 from 9 to 1
move 2 from 9 to 1
move 10 from 2 to 7
move 4 from 3 to 1
move 1 from 8 to 3
move 1 from 4 to 5
move 1 from 3 to 6
move 1 from 2 to 1
move 10 from 1 to 3
move 1 from 4 to 7
move 1 from 6 to 4
move 7 from 3 to 2
move 5 from 2 to 8
move 11 from 7 to 2
move 3 from 4 to 3
move 1 from 4 to 3
move 5 from 8 to 9
move 17 from 2 to 4
move 11 from 1 to 5
move 4 from 1 to 3
move 5 from 9 to 2
move 4 from 2 to 1
move 3 from 5 to 7
move 6 from 5 to 3
move 1 from 5 to 8
move 6 from 1 to 8
move 3 from 8 to 5
move 1 from 1 to 4
move 1 from 7 to 2
move 15 from 3 to 4
move 1 from 1 to 3
move 10 from 3 to 9
move 2 from 7 to 4
move 1 from 2 to 8
move 21 from 4 to 9
move 1 from 2 to 3
move 1 from 8 to 1
move 9 from 4 to 2
move 1 from 1 to 5
move 5 from 2 to 7
move 2 from 8 to 5
move 1 from 8 to 1
move 2 from 2 to 8
move 2 from 4 to 9
move 24 from 9 to 5
move 3 from 4 to 1
move 2 from 2 to 5
move 12 from 5 to 1
move 10 from 1 to 5
move 23 from 5 to 6
move 8 from 9 to 1
move 3 from 8 to 1
move 1 from 1 to 2
move 1 from 3 to 7
move 11 from 6 to 1
move 1 from 2 to 4
move 6 from 6 to 8
move 4 from 6 to 7
move 1 from 7 to 3
move 1 from 3 to 4
move 23 from 1 to 8
move 1 from 4 to 2
move 1 from 2 to 1
move 1 from 6 to 7
move 6 from 5 to 3
move 1 from 7 to 8
move 1 from 1 to 8
move 1 from 9 to 3
move 6 from 7 to 2
move 3 from 5 to 9
move 5 from 2 to 3
move 28 from 8 to 3
move 4 from 1 to 9
move 5 from 9 to 5
move 2 from 8 to 5
move 1 from 9 to 4
move 2 from 7 to 5
move 1 from 4 to 2
move 1 from 4 to 8
move 2 from 8 to 3
move 6 from 5 to 2
move 1 from 7 to 2
move 39 from 3 to 2
move 2 from 3 to 8
move 1 from 9 to 6
move 2 from 2 to 9
move 2 from 9 to 6
move 1 from 8 to 1
move 1 from 1 to 6
move 5 from 6 to 9
move 2 from 5 to 8
move 20 from 2 to 4
move 2 from 4 to 8
move 2 from 8 to 3
move 3 from 3 to 1
move 22 from 2 to 5
move 2 from 9 to 1
move 3 from 1 to 7
move 1 from 2 to 6
move 1 from 2 to 9
move 1 from 1 to 8
move 2 from 7 to 9
move 1 from 6 to 8
move 1 from 2 to 7
move 1 from 1 to 3
move 1 from 9 to 8
move 1 from 8 to 5
move 3 from 8 to 7
move 3 from 7 to 8
move 15 from 4 to 1
move 1 from 4 to 3
move 10 from 1 to 6
move 3 from 8 to 1
move 5 from 9 to 4
move 7 from 5 to 1
move 4 from 6 to 3
move 15 from 5 to 2
move 4 from 6 to 4
move 7 from 2 to 1
move 6 from 4 to 6
move 1 from 5 to 9
move 1 from 5 to 7
move 1 from 3 to 5
move 11 from 1 to 8
move 3 from 4 to 6
move 4 from 1 to 5
move 1 from 2 to 5
move 2 from 8 to 3
move 11 from 6 to 1
move 1 from 3 to 7
move 1 from 9 to 8
move 6 from 5 to 8
move 3 from 8 to 4
move 1 from 4 to 5
move 3 from 3 to 1
move 9 from 8 to 2
move 2 from 1 to 5
move 11 from 2 to 5
move 1 from 3 to 6
move 2 from 8 to 5
move 3 from 4 to 6
move 1 from 8 to 3
move 2 from 1 to 9
move 1 from 3 to 8
move 16 from 5 to 7
move 3 from 1 to 6
move 1 from 3 to 5
move 1 from 6 to 7
move 1 from 9 to 4
move 1 from 5 to 4
move 1 from 3 to 2
move 1 from 1 to 2
move 3 from 4 to 9
move 1 from 2 to 7
move 2 from 8 to 3
move 6 from 2 to 8
move 11 from 1 to 3
move 6 from 3 to 1
move 4 from 3 to 2
move 2 from 3 to 1
move 1 from 1 to 3
move 4 from 8 to 4
move 4 from 8 to 2
move 11 from 7 to 2
move 9 from 7 to 5
move 1 from 7 to 3
move 4 from 5 to 7
move 14 from 2 to 3
move 17 from 3 to 7
move 2 from 5 to 2
move 1 from 5 to 7
move 1 from 5 to 6
move 4 from 6 to 7
move 8 from 1 to 2
move 2 from 6 to 4
move 1 from 6 to 8
move 6 from 4 to 1
move 1 from 8 to 5
move 6 from 7 to 8
move 5 from 8 to 3
move 12 from 2 to 1
move 1 from 8 to 4
move 4 from 3 to 1
move 4 from 2 to 4
move 3 from 9 to 3
move 3 from 3 to 2
move 1 from 3 to 2
move 3 from 4 to 1
move 2 from 5 to 7
move 22 from 1 to 8
move 17 from 8 to 6
move 21 from 7 to 6
move 3 from 2 to 8
move 3 from 1 to 5
move 3 from 5 to 2
move 2 from 4 to 6
move 7 from 6 to 5
move 1 from 9 to 4
move 14 from 6 to 4
move 5 from 8 to 3
move 1 from 6 to 3
move 3 from 3 to 9
move 2 from 9 to 1
move 2 from 7 to 1
move 16 from 6 to 8
move 2 from 6 to 7
move 1 from 2 to 7
move 1 from 3 to 8
move 7 from 4 to 1
move 2 from 7 to 2
move 4 from 4 to 7
move 5 from 2 to 4
move 1 from 7 to 3
move 3 from 5 to 8
move 1 from 7 to 5
move 12 from 1 to 6
move 3 from 7 to 2
move 7 from 4 to 2
move 3 from 3 to 2
move 1 from 4 to 2
move 1 from 9 to 8
move 8 from 6 to 8
move 12 from 2 to 4
move 5 from 5 to 2
move 11 from 4 to 9
move 3 from 6 to 3
move 2 from 4 to 2
move 4 from 2 to 6
move 5 from 2 to 8
move 12 from 8 to 4
move 20 from 8 to 5
move 13 from 5 to 3
move 1 from 8 to 5
move 5 from 5 to 9
move 16 from 9 to 1
move 9 from 4 to 5
move 12 from 3 to 9
move 5 from 6 to 5
move 9 from 9 to 7
move 14 from 1 to 4
move 14 from 4 to 1
move 15 from 5 to 7
move 4 from 8 to 2
move 3 from 4 to 3
move 3 from 1 to 8
move 1 from 5 to 9
move 1 from 5 to 3
move 3 from 9 to 8
move 4 from 3 to 4
move 1 from 4 to 6
move 20 from 7 to 2
move 2 from 3 to 8
move 3 from 7 to 2
move 4 from 2 to 1
move 1 from 6 to 7
move 3 from 4 to 2
move 2 from 2 to 3
move 4 from 3 to 4
move 1 from 8 to 1
move 3 from 8 to 1
move 2 from 7 to 8
move 1 from 4 to 5
move 14 from 2 to 5
move 6 from 1 to 5
move 1 from 4 to 3
move 15 from 1 to 4
move 1 from 8 to 2
move 1 from 9 to 5
move 4 from 8 to 7
move 13 from 5 to 6
move 1 from 8 to 1
move 2 from 7 to 9
move 12 from 6 to 4
move 1 from 3 to 6
move 1 from 1 to 6
move 4 from 5 to 2
move 5 from 5 to 6
move 2 from 6 to 2
move 1 from 7 to 5
move 2 from 6 to 9
move 1 from 5 to 9
move 16 from 2 to 5
move 17 from 4 to 1
move 3 from 1 to 3
move 1 from 2 to 6
move 2 from 6 to 1
move 3 from 3 to 1
move 14 from 1 to 8
move 3 from 5 to 2
move 4 from 8 to 2
move 3 from 4 to 5
move 15 from 5 to 3
move 1 from 7 to 6
move 3 from 1 to 8
move 2 from 3 to 7
move 1 from 1 to 2
move 1 from 7 to 6
move 4 from 2 to 8
move 2 from 6 to 2
move 1 from 7 to 6
move 3 from 8 to 2
move 12 from 8 to 6
move 1 from 5 to 6
move 3 from 2 to 5
move 2 from 2 to 5
move 4 from 6 to 5
move 4 from 3 to 5
move 1 from 8 to 4
move 11 from 6 to 4
move 6 from 3 to 1
move 2 from 9 to 8
move 20 from 4 to 5
move 1 from 4 to 9
move 2 from 3 to 8
move 1 from 3 to 8
move 17 from 5 to 8
move 5 from 5 to 9
move 9 from 5 to 1
move 2 from 6 to 7
move 23 from 8 to 2
move 2 from 7 to 5
move 3 from 9 to 4
move 16 from 2 to 4
move 11 from 1 to 8
move 4 from 5 to 8
move 11 from 2 to 6
move 2 from 6 to 1
move 5 from 9 to 5
move 5 from 5 to 6
move 5 from 8 to 6
move 1 from 6 to 7
move 7 from 8 to 1
move 12 from 1 to 2
move 1 from 9 to 5
move 1 from 1 to 3
move 1 from 1 to 4
move 1 from 5 to 3
move 1 from 3 to 6
move 1 from 8 to 2
move 18 from 6 to 2
move 1 from 6 to 2
move 2 from 8 to 3
move 3 from 3 to 8
move 18 from 4 to 9
move 11 from 9 to 2
move 2 from 9 to 6
move 2 from 4 to 1
move 1 from 1 to 5
move 1 from 5 to 4
move 1 from 4 to 8
move 42 from 2 to 1
move 3 from 9 to 3
move 1 from 8 to 1
move 1 from 3 to 4
move 3 from 8 to 7
move 1 from 4 to 1
move 2 from 3 to 2
move 17 from 1 to 6
move 15 from 6 to 3
move 2 from 9 to 7
move 1 from 3 to 6
move 2 from 7 to 6
move 2 from 2 to 4
move 1 from 2 to 3
move 1 from 4 to 9
move 1 from 4 to 1
move 1 from 6 to 3
move 20 from 1 to 9
move 6 from 1 to 9
move 7 from 9 to 3
move 20 from 9 to 1
move 1 from 6 to 7
move 2 from 6 to 7
move 1 from 6 to 5
move 1 from 6 to 8
move 4 from 7 to 3
move 3 from 7 to 2
move 1 from 6 to 4
move 1 from 2 to 1
move 1 from 4 to 9
move 21 from 3 to 2
move 5 from 3 to 8
move 1 from 5 to 1
move 2 from 8 to 7
move 4 from 8 to 3
move 4 from 2 to 5
move 19 from 2 to 3
move 1 from 9 to 2
move 23 from 3 to 2
move 2 from 7 to 4
move 3 from 5 to 9
move 16 from 2 to 1
move 1 from 5 to 4
move 1 from 9 to 3
move 2 from 3 to 8
move 3 from 4 to 6
move 1 from 6 to 2
move 1 from 8 to 6
move 5 from 2 to 6
move 7 from 6 to 5
move 4 from 2 to 6
move 6 from 5 to 9
move 1 from 8 to 4
move 18 from 1 to 9
move 1 from 5 to 2
move 9 from 9 to 4
move 5 from 6 to 3
move 9 from 4 to 1
move 4 from 9 to 2
move 1 from 4 to 8
move 1 from 8 to 3
move 7 from 1 to 8
move 6 from 3 to 2
move 10 from 2 to 9
move 21 from 1 to 8
move 1 from 2 to 8
move 19 from 8 to 4
move 1 from 8 to 3
move 16 from 4 to 8
move 1 from 4 to 2
move 2 from 1 to 5
move 1 from 2 to 3
move 1 from 4 to 5
move 1 from 4 to 8
move 2 from 1 to 3
move 3 from 3 to 2
move 5 from 9 to 1
move 1 from 3 to 4
move 4 from 9 to 4
move 2 from 1 to 9
move 2 from 2 to 5
move 1 from 2 to 7
move 3 from 1 to 7
move 10 from 8 to 6
move 4 from 8 to 5
move 3 from 4 to 3
move 3 from 3 to 4
move 1 from 9 to 8
move 2 from 7 to 2
move 1 from 2 to 1
move 4 from 9 to 3"""
    # 0  1   2  3  4 5
    for command in commands.split("\n"):
        if command == "":
            continue
        command = command.split(" ")
        if command[0] == "move":
            for i in range(int(command[1])):
                from_stack = int(command[3]) - 1
                to_stack = int(command[5]) - 1
                stacks[to_stack].append(stacks[from_stack].pop())
        else:
            print("Invalid command: " + command)

    for stack in stacks:
        print(stack[-1], end="")
    print()

    stacks[0] = ["D", "T", "W", "F", "J", "S", "H", "N"]
    stacks[1] = ["H", "R", "P", "Q", "T", "N", "B", "G"]
    stacks[2] = [
        "L",
        "Q",
        "V",
    ]
    stacks[3] = ["N", "B", "S", "W", "R", "Q"]
    stacks[4] = ["N", "D", "F", "T", "V", "M", "B"]
    stacks[5] = ["M", "D", "B", "V", "H", "T", "R"]
    stacks[6] = ["D", "B", "Q", "J"]
    stacks[7] = ["D", "N", "J", "V", "R", "Z", "H", "Q"]
    stacks[8] = ["B", "N", "H", "M", "S"]
    for command in commands.split("\n"):
        if command == "":
            continue
        command = command.split(" ")
        if command[0] == "move":
            from_stack = int(command[3]) - 1
            to_stack = int(command[5]) - 1
            index = int(command[1])
            stacks[to_stack].extend(stacks[from_stack][-index:])
            del stacks[from_stack][-index:]
        else:
            print("Invalid command: " + command)

    for stack in stacks:
        print(stack[-1], end="")


if __name__ == "__main__":
    main()