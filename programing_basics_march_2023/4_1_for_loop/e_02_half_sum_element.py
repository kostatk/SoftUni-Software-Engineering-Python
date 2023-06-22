from sys import maxsize

n = int(input())

total_sum = 0
max_number = -maxsize

for _ in range(n):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

diff = abs(max_number - (total_sum - max_number))

if diff == 0:
    print("Yes")
    print("Sum =", max_number)
else:
    print("No")
    print("Diff =", diff)
