def solve1(text):
    pass

def solve2(text):
    pass

if __name__ == '__main__':
    test1 = open("test1", "r").read().split("\n")
    test2 = open("test2", "r").read().split("\n")
    input = open("input", "r").read().split("\n")

    test1_solution = 0
    test2_solution = 0

    print("Test 1: " + str(solve1(test1)))
    if test1_solution != solve1(test1):
        print("Test 1 failed!")
        exit(1)

    print("Solution 1: " + str(solve1(input)))
    
    print("Test 2: " + str(solve2(test2)))
    if test2_solution != solve2(test2):
        print("Test 2 failed!")
        exit(1)

    print("Solution 2: " + str(solve2(input)))

