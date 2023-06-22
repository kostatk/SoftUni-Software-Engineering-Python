number = int(input())

current_sum = 0

for checked_number in range (1, number + 1):
    checked_number = str(checked_number)
    for i in range(len(checked_number)):
        current_sum += int(checked_number[i])
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{checked_number} -> True")
    else:
        print(f"{checked_number} -> False")
    current_sum = 0

