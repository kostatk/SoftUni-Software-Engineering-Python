numbers = int(input())

total_sum = 0

for i in range(numbers):
    curr_number = int(input())
    total_sum += curr_number

average = total_sum / numbers

print(f"{average:.2f}")
