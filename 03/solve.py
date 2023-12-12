def solve1(text):
    sum = 0
    # Find number
    # Every line
    for i in range(len(text)):
        # Every character
        for j in range(len(text[i])):
            i_start = 0
            if text[i][j].isnumeric() and (not text[i][j-1].isnumeric() or j == 0):
                # Number start found 
                i_start = j
                i_end = j
                for k in range(j, len(text[i]) + 1):
                    if k == len(text[i]):
                        # Number end found
                        i_end = k
                        break
                    elif not text[i][k].isnumeric():
                        # Number end found
                        i_end = k - 1
                        break

                # Scan for surrounding markers
                scan_x_start = max(0, i_start - 1)
                scan_x_end = min(len(text[i]) - 1, i_end + 1)
                scan_y_start = max(0, i - 1)
                scan_y_end = min(len(text) - 1, i + 1)

                num = int(text[i][i_start:i_end+1])

                for x in range(scan_x_start, scan_x_end + 1):
                    for y in range(scan_y_start, scan_y_end + 1):
                        if text[y][x] == ".":
                            continue
                        if text[y][x].isnumeric():
                            continue
                        
                        sum += num
    return sum


def solve2(text):
    sum = 0
    gears = {}
    # Find number
    # Every line
    for i in range(len(text)):
        # Every character
        for j in range(len(text[i])):
            i_start = 0
            if text[i][j].isnumeric() and (not text[i][j-1].isnumeric() or j == 0):
                # Number start found 
                i_start = j
                i_end = j
                for k in range(j, len(text[i]) + 1):
                    if k == len(text[i]):
                        # Number end found
                        i_end = k
                        break
                    elif not text[i][k].isnumeric():
                        # Number end found
                        i_end = k - 1
                        break

                # Scan for surrounding markers
                scan_x_start = max(0, i_start - 1)
                scan_x_end = min(len(text[i]) - 1, i_end + 1)
                scan_y_start = max(0, i - 1)
                scan_y_end = min(len(text) - 1, i + 1)

                num = int(text[i][i_start:i_end+1])

                for x in range(scan_x_start, scan_x_end + 1):
                    for y in range(scan_y_start, scan_y_end + 1):
                        if text[y][x] == ".":
                            continue
                        if text[y][x].isnumeric():
                            continue
                        
                        # print("Found " + str(num) + " at " + str(x) + ", " + str(y) + " with marker " + text[y][x])
                        if text[y][x] != "*":
                            continue
                        if f"{x}_{y}" not in gears:
                            gears[f"{x}_{y}"] = []
                        gears[f"{x}_{y}"].append(num)
    for gear in gears:
        if len(gears[gear]) > 1:
            sum += min(gears[gear]) * max(gears[gear])
    return sum

if __name__ == '__main__':
    test1 = open("test1", "r").read().split("\n")
    test2 = open("test2", "r").read().split("\n")
    input = open("input", "r").read().split("\n")

    test1_solution = 4361
    test2_solution = 467835

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

