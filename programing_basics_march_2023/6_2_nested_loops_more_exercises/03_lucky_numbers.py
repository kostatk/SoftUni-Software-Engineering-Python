number = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        if number % (a + b) != 0:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if a + b == c + d:
                    print(f"{a}{b}{c}{d}", end=" ")
