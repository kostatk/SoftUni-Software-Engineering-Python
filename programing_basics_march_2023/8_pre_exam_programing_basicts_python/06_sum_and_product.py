num_n = int(input())

IS_COMBINATION = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                if a + b + c + d == a * b * d * c and num_n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    IS_COMBINATION = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and num_n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    IS_COMBINATION = True
                    break
            if IS_COMBINATION:
                break
        if IS_COMBINATION:
            break
    if IS_COMBINATION:
        break


if not IS_COMBINATION:
    print(f"Nothing found")
