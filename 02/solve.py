limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def solve1(text):
    sum = 0
    for i in range(len(text)):
        if text[i] == "":
            continue
        validGame = True
        reveals = text[i].split(":")[1].split(";")
        for j in range(len(reveals)):
            entries = reveals[j].split(",")
            for k in range(len(entries)):
                count = entries[k].strip().split(" ")[0]
                color = entries[k].strip().split(" ")[1]
                if int(count) > limit[color]:
                    validGame = False
                    break
            if not validGame:
                break
        if validGame:
            sum += i + 1

    return sum

def solve2(text):
    sum = 0
    for i in range(len(text)):
        if text[i] == "":
            continue
        validGame = True
        min_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        reveals = text[i].split(":")[1].split(";")
        for j in range(len(reveals)):
            entries = reveals[j].split(",")
            for k in range(len(entries)):
                count = entries[k].strip().split(" ")[0]
                color = entries[k].strip().split(" ")[1]
                if int(count) > min_cubes[color]:
                    min_cubes[color] = int(count)
        sum += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    return sum

if __name__ == '__main__':
    test1 = open("test1", "r").read().split("\n")
    test2 = open("test2", "r").read().split("\n")
    input = open("input", "r").read().split("\n")

    test1_solution = 8
    test2_solution = 2286

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

