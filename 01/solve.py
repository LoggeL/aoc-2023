# Day 1

input_file = open("input", "r")
input = input_file.read().split("\n")

def leftMostNumber(text):
    for i in range(len(text)):
        if text[i].isnumeric():
            return text[i]
        for j in range(len(replacements)):
            if text[i:].startswith(replacements[j]):
                return str(j+1)
        
def rightMostNumber(text):
    for i in range(len(text)-1, -1, -1):
        if text[i].isnumeric():
            return text[i]
        for j in range(len(replacements)):
            if text[i:].startswith(replacements[j]):
                return str(j+1)
        

solution = 0

replacements = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

for line in input:
    if line == "":
        continue
    left = leftMostNumber(line)
    right = rightMostNumber(line)
    solution += int(left + right)

print("Solution: " + str(solution))