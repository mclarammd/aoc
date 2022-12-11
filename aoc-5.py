stacks = [
    ["S", "Z", "P", "D", "L", "B", "F", "C"],
    ["N", "V", "G", "P", "H", "W", "B"],
    ["F", "W", "B", "J", "G"],
    ["G", "J", "N", "F", "L", "W", "C", "S"],
    ["W", "J", "L", "T", "P", "M", "S", "H"],
    ["B", "C", "W", "G", "F", "S"],
    ["H", "T", "P", "M", "Q", "B", "W"],
    ["F", "S", "W", "T"],
    ["N", "C", "R"]
]

while True:
    try:
        line = input().split()
        n, f, t = int(line[1]), int(line[3]), int(line[5])
        while n:
            element = stacks[f - 1].pop()
            stacks[t - 1].append(element)
            n -=1
    except:
        break

ans = ""
for s in stacks:
    ans += stacks[s][-1]

print(ans)

###### 2

stacks = [
    ["S", "Z", "P", "D", "L", "B", "F", "C"],
    ["N", "V", "G", "P", "H", "W", "B"],
    ["F", "W", "B", "J", "G"],
    ["G", "J", "N", "F", "L", "W", "C", "S"],
    ["W", "J", "L", "T", "P", "M", "S", "H"],
    ["B", "C", "W", "G", "F", "S"],
    ["H", "T", "P", "M", "Q", "B", "W"],
    ["F", "S", "W", "T"],
    ["N", "C", "R"]
]

while True:
    try:
        line = input().split()
        n, f, t = int(line[1]), int(line[3]), int(line[5])
        stacks[t - 1] += stacks[f - 1][len(stacks[f - 1]) - n:]
        stacks[f-1] = stacks[f-1][:len(stacks[f - 1]) - n]
        # while n:
        #     element = stacks[f - 1].pop()
        #     stacks[t - 1].append(element)
        #     n -=1
    except:
        break

ans = ""
for s in stacks:
    ans += s[-1]

print(ans)
