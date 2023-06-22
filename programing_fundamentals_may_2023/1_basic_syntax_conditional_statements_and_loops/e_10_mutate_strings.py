first_string = input()
second_string = input()
last_printed_word = ""

for character in range(len(first_string)):
    left_part = second_string[0:character + 1]
    right_part = first_string[character + 1:]
    new_word = left_part + right_part
    if new_word != last_printed_word and new_word != first_string:
        print(new_word)
    last_printed_word = new_word
