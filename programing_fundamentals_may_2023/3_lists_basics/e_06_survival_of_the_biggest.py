my_list = input().split()
integer_list = []
for element in my_list:
    integer_list.append(int(element))
numbers_to_remove = int(input())

copied_list = integer_list.copy()
copied_list.sort()

for rolls in range(numbers_to_remove):
    for element in integer_list:
        if element == copied_list[0]:
            integer_list.remove(element)
            copied_list.remove(copied_list[0])
            break

list_to_print = []
for element in integer_list:
    list_to_print.append(str(element))

print(", ".join(list_to_print))
