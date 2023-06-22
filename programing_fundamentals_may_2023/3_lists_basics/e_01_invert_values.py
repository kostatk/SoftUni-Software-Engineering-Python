string = input()
list_of_stings = string.split(" ")
# print(list_of_stings)

list_of_numbers = []
for string in list_of_stings:
    list_of_numbers.append(-int(string))
print(list_of_numbers)
