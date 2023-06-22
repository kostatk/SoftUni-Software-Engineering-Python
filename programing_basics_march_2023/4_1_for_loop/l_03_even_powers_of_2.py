from math import pow

num = int(input())
result = 0

for power in range (0, num + 1):
    if power % 2 == 0:
        result = pow(2, power)
        print(int(result))
