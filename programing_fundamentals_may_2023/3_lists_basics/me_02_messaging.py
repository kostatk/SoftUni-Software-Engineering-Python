list_of_numbers_as_strings = input().split()

string = input()
list_of_chars = []
for ch in string:
    list_of_chars.append(ch)

final_list = []

for check in range(len(list_of_numbers_as_strings)):
    current_sum = 0
    for digit in list_of_numbers_as_strings[check]:
        current_sum += int(digit)
    if current_sum < len(list_of_chars):
        final_list.append(list_of_chars[current_sum])
        list_of_chars.remove(list_of_chars[current_sum])
    else:
        final_list.append(list_of_chars[current_sum - len(list_of_chars)])
        list_of_chars.remove(list_of_chars[current_sum - len(list_of_chars)])

print("".join(final_list))
