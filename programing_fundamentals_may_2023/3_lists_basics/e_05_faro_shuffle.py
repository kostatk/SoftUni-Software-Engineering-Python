initial_list = input().split()
number_of_faro_shuffles = int(input())
length_of_list = len(initial_list)
list_a = []
list_b = []

for shuffle in range(number_of_faro_shuffles):
    for index in range(0, length_of_list // 2):
        list_a.append(initial_list[index])
    for index in range(length_of_list // 2, length_of_list):
        list_b.append(initial_list[index])
    initial_list.clear()
    for index in range(0, length_of_list // 2):
        initial_list.append(list_a[index])
        initial_list.append(list_b[index])
    list_a.clear()
    list_b.clear()

print(initial_list)


