
def calculator(operator, num_a, num_b):
    if operator == "multiply":
        return num_a * num_b
    elif operator == "divide":
        if num_b != 0:
            return num_a // num_b
    elif operator == "add":
        return num_a + num_b
    elif operator == "subtract":
        return num_a - num_b


user_operator = input()
user_number_one = int(input())
user_number_two = int(input())

print(calculator(user_operator, user_number_one, user_number_two))
