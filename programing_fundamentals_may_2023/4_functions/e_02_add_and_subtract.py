def sum_numbers(a, b):
    return a + b


def subtract(d, c):
    return d - c


def add_and_subtract(a_from_input, b_from_input, c_from_input):
    d_sum = sum_numbers(a_from_input, b_from_input)
    return subtract(d_sum, c_from_input)


user_a = int(input())
user_b = int(input())
user_c = int(input())

print(add_and_subtract(user_a, user_b, user_c))
