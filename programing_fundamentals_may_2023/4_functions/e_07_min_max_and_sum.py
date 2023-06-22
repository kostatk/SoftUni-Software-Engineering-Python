from sys import maxsize


def min_number(a):
    min_result = maxsize
    for number in a:
        if number < min_result:
            min_result = number
    return min_result


def max_number(a):
    max_result = -maxsize
    for number in a:
        if number > max_result:
            max_result = number
    return max_result


def sum_numbers(a):
    sum_result = 0
    for number in a:
        sum_result += number
    return sum_result


input_string_list = input().split()
list_of_numbers = []
for element in input_string_list:
    list_of_numbers.append(int(element))

minimum_number = min_number(list_of_numbers)
maximum_number = max_number(list_of_numbers)
sum_of_all_numbers = sum_numbers(list_of_numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")

# Това е късата версия, която не ни учи на нищо
# print(f"The minimum number is {min(list_of_numbers)}")
# print(f"The maximum number is {max(list_of_numbers)}")
# print(f"The sum number is: {sum(list_of_numbers)}")
