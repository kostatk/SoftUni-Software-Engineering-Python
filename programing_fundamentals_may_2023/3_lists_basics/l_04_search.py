number_of_elements = int(input())
word = input()

list_of_strings = []
list_of_included = []

for string in range(number_of_elements):
    current_string = input()
    list_of_strings.append(current_string)

for element in list_of_strings:
    if word in element:
        list_of_included.append(element)

print(list_of_strings)
print(list_of_included)
