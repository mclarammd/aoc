curr = 0
points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}
# winning_comb = ["CX", "BZ", "AY"]
winning_comb = {
    "C": "X",
    "B": "Z",
    "A": "Y"
}
# eq = ["AX", "BY", "CZ"]
loosing_comb = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}
while True:
    try:
        a = input().split()
        if a[1] == "Y":
            curr += points[a[0]] + 3
        else:
            if a[1] == "Z":
                curr += points[winning_comb[a[0]]] + 6
            else:
                curr += points[loosing_comb[a[0]]]
    except EOFError:
        break

print(curr)
