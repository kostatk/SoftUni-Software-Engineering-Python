number_of_elements = int(input())

list_of_numbers = []
formatted_list = []

for number in range(number_of_elements):
    list_of_numbers.append(int(input()))

command = input()
for element in list_of_numbers:
    if command == "even" and element % 2 == 0:
        formatted_list.append(element)
    elif command == "odd" and element % 2 != 0:
        formatted_list.append(element)
    elif command == "negative" and element < 0:
        formatted_list.append(element)
    elif command == "positive" and element >= 0:
        formatted_list.append(element)

# print(list_of_numbers)
print(formatted_list)
