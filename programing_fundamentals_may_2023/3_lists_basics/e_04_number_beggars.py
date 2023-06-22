input_line = input()
count_of_beggars = int(input())
list_of_strings = input_line.split(", ")
list_of_numbers = []
for string in list_of_strings:
    list_of_numbers.append(int(string))

final_list_of_sums = []
beggar_index = 0

for beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for index in range(beggar_index, len(list_of_numbers), count_of_beggars):
        current_beggar_sum += list_of_numbers[index]
    final_list_of_sums.append(current_beggar_sum)
    beggar_index += 1

# print(list_of_numbers)
print(final_list_of_sums)
