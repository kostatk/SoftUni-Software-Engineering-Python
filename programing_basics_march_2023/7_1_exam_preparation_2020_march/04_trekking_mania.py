groups_count = int(input())

musala_counter = 0
monblan_counter = 0
kiliman_counter = 0
k2_counter = 0
everest_counter = 0

for g in range(groups_count):
    curr_group_number = int(input())
    if curr_group_number <= 5:
        musala_counter += curr_group_number
    elif 6 <= curr_group_number <= 12:
        monblan_counter += curr_group_number
    elif 13 <= curr_group_number <= 25:
        kiliman_counter += curr_group_number
    elif 26 <= curr_group_number <= 40:
        k2_counter += curr_group_number
    elif 41 <= curr_group_number:
        everest_counter += curr_group_number

total_climbers = musala_counter + monblan_counter + kiliman_counter + k2_counter + everest_counter

print(f"{musala_counter / total_climbers * 100:.2f}%")
print(f"{monblan_counter / total_climbers * 100:.2f}%")
print(f"{kiliman_counter / total_climbers * 100:.2f}%")
print(f"{k2_counter / total_climbers * 100:.2f}%")
print(f"{everest_counter / total_climbers * 100:.2f}%")
