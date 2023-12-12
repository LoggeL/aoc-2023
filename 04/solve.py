def solve1(text):
    sum = 0
    for line in text:
        # Remove Card \d:
        wins = 0
        line = line.split(":")[1]
        left = line.split("|")[0].strip()
        right = line.split("|")[1].strip()

        left_nums = [int(x.strip()) for x in left.split()]
        right_nums = [int(x.strip()) for x in right.split()]

        for left_num in left_nums:
            if left_num in right_nums:
                wins += 1

        sum += 2 ** (wins - 1) if wins > 0 else 0

    return sum

def solve2(text):
    card_wins = [1 for x in range(0, len(text))]
    for i in range(len(text)):
        # Remove Card \d:
        line = text[i]
        wins = 0
        line = line.split(":")[1]
        left = line.split("|")[0].strip()
        right = line.split("|")[1].strip()

        left_nums = [int(x.strip()) for x in left.split()]
        right_nums = [int(x.strip()) for x in right.split()]

        for left_num in left_nums:
            if left_num in right_nums:
                wins += 1
    
        for j in range(wins):
            card_wins[i + j + 1] += card_wins[i]

    return sum(card_wins)

if __name__ == '__main__':
    test1 = open("test1", "r").read().split("\n")
    test2 = open("test2", "r").read().split("\n")
    input = open("input", "r").read().split("\n")

    test1_solution = 13
    test2_solution = 30

    test1_result = solve1(test1)
    test2_result = solve2(test2)
    
    print("Test 1: " + str(test1_result))
    if test1_solution != test1_result:
        print("Test 1 failed!")
        exit(1)

    print("Solution 1: " + str(solve1(input)))
    
    print("Test 2: " + str(test2_result))
    if test2_solution != test2_result:
        print("Test 2 failed!")
        exit(1)

    print("Solution 2: " + str(solve2(input)))
