
def strings_between_letters_in_ascii(a, b):
    for digit in range(ord(a) + 1, ord(b)):
        print(chr(digit), end=" ")


user_input_string_one = input()
user_input_string_two = input()
strings_between_letters_in_ascii(user_input_string_one, user_input_string_two)
