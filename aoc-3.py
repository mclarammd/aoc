import string

sum_priorities = 0
priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
p_map = {}
for i in range(len(priorities)):
    p_map[priorities[i]] = i + 1

while True:
    try:
        line = input()
        r1, r2 = line[:len(line)//2], line[len(line)//2:]
        for c in r1:
            if c in r2:
                sum_priorities += p_map[c]
                break
    except EOFError:
        break

print(sum_priorities)

######### part 2

import string

sum_priorities = 0
priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
p_map = {}
for i in range(len(priorities)):
    p_map[priorities[i]] = i + 1

groups = []

def find_badge(group):
    for c in group[0]:
        if c in group[1] and c in group[2]:
            return c

while True:
    try:
        line = input()
        groups.append(line)

        if len(groups) == 3:
            badge = find_badge(groups)
            sum_priorities += p_map[badge]
            groups = []
    except EOFError:
        break

print(sum_priorities)
