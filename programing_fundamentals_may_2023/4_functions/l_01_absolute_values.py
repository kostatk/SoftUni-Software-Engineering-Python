list_of_values = input().split()
list_of_absolutes = []

for element in list_of_values:
    current_element = float(element)
    list_of_absolutes.append(abs(current_element))

print(list_of_absolutes)
