contain_all = 0
while True:
    try:
        elf_intervals = input().split(",")
        interval1, interval2 = list(map(int, elf_intervals[0].split("-"))), list(map(int, elf_intervals[1].split("-")))
        # print(interval1, interval2)
        if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
            contain_all += 1
        elif interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
            contain_all += 1

    except:
        break

print(contain_all)

######### part 2

contain_all = 0
while True:
    try:
        elf_intervals = input().split(",")
        interval1, interval2 = list(map(int, elf_intervals[0].split("-"))), list(map(int, elf_intervals[1].split("-")))
        # print(interval1, interval2)
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            continue
        else:
            contain_all += 1

    except:
        break

print(contain_all)
