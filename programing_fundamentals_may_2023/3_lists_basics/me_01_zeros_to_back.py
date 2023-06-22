list_of_strings = input().split(", ")
list_of_numbers = []
for element in list_of_strings:
    list_of_numbers.append(int(element))

for index in range(len(list_of_numbers) - 1, -1, -1):
    if list_of_numbers[index] == 0:
        list_of_numbers.append(list_of_numbers.pop(index))

print(list_of_numbers)