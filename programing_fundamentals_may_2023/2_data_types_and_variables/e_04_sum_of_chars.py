number_of_characters = int(input())
sum_of_all_codes = 0

for character in range(number_of_characters):
    current_character = input()
    sum_of_all_codes += ord(current_character)

print(f"The sum equals: {sum_of_all_codes}")
