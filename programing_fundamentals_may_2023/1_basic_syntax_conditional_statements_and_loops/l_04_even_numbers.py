numbers_for_input = int(input())

for number in range(numbers_for_input):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break
else:
    print("All numbers are even.")
