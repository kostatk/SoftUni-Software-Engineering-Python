beginning_num = int(input())
ending_num = int(input())

for a in range (beginning_num, ending_num + 1):
    for b in range(beginning_num, ending_num + 1):
        for c in range(beginning_num, ending_num + 1):
            for d in range(beginning_num, ending_num + 1):
                if (a % 2 == 0 and d % 2 != 0) or (a % 2 != 0 and d % 2 == 0):
                    if a > d and (b + c) % 2 == 0:
                        print(f"{a}{b}{c}{d}", end=" ")
