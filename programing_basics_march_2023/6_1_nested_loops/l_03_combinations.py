n = int(input())

combinations = 0

for x_1 in range(0, n + 1):
    for x_2 in range(0, n + 1):
        for x_3 in range(0, n + 1):
            if x_1 + x_2 + x_3 == n:
                combinations += 1

print(combinations)





# x1 + x2 + x3 = n