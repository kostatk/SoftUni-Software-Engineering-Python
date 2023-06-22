
def smallest_number(a, b, c):
    check_list = [a, b, c]
    check_list.sort()
    return check_list[0]


user_input_number_a = int(input())
user_input_number_b = int(input())
user_input_number_c = int(input())

print(smallest_number(user_input_number_a, user_input_number_b, user_input_number_c))


# Това е решението от упражнението:
# def smallest_number(some_numbers):
#     min_number = min(some_numbers)
#     return min_number
#
#
# user_input_number_a = int(input())
# user_input_number_b = int(input())
# user_input_number_c = int(input())
# numbers = [user_input_number_a, user_input_number_b, user_input_number_c]
# print(smallest_number(numbers))
