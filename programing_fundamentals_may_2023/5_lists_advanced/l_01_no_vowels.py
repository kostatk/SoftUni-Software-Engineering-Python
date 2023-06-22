input_word = input()

check_list = ['a', 'o', 'u', 'e', 'i']

print_word = [ch for ch in input_word if ch.lower() not in check_list]

print("".join(print_word))
