
sum_simple_numbers = 0
sum_non_simple_numbers = 0
IS_PRIME = True

while True:
    command = input()
    if command == "stop":
        break
    cur_number = int(command)
    if cur_number < 0:
        print("Number is negative.")
        continue
    # if cur_number == 1 or cur_number == 2: # 1 не е просто число,
    #     sum_simple_numbers += cur_number   # a при 2 не влиза в проверката за просто и директно го смята за просто
    #     continue                            # затова цялото това трябва да се махне
    for n in range(2, cur_number):
        if cur_number % n == 0:
            IS_PRIME = False
            sum_non_simple_numbers += cur_number
            break
    if IS_PRIME:
        sum_simple_numbers += cur_number

    IS_PRIME = True

print(f"Sum of all prime numbers is: {sum_simple_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_simple_numbers}")


