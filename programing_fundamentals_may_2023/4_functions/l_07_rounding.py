
user_numbers_as_strings = input().split()

final_list_of_numbers = []

for element in user_numbers_as_strings:
    current_element = float(element)
    final_list_of_numbers.append(round(current_element))

print(final_list_of_numbers)

