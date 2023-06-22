first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

for first in range(1, first_digit_limit + 1):
    if first % 2 != 0:
        continue
    for second in range(1, second_digit_limit + 1):
        if second < 2 or second > 7:
            continue
        if second == 4 or second == 6:
            continue
        for third in range(1, third_digit_limit + 1):
            if third % 2 != 0:
                continue
            print(f"{first} {second} {third}")

