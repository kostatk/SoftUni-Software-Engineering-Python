number_electrons = int(input())
distributed_list = []
index_n = 0

while number_electrons > 0:
    index_n += 1
    current_electrons = 2 * index_n ** 2
    if current_electrons <= number_electrons:
        distributed_list.append(current_electrons)
    else:
        distributed_list.append(number_electrons)
    number_electrons -= current_electrons

print(distributed_list)
