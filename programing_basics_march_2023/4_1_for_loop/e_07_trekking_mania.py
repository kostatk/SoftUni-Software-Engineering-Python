num_groups = int(input())

musa_count = 0
monbl_count = 0
kili_count = 0
k_2_count = 0
ever_count = 0
total_counter = 0

for _ in range(num_groups):
    cur_group_count = int(input())
    total_counter += cur_group_count
    if cur_group_count <= 5:
       musa_count += cur_group_count
    elif 6 <= cur_group_count <= 12:
       monbl_count += cur_group_count
    elif 13 <= cur_group_count <= 25:
       kili_count += cur_group_count
    elif 26 <= cur_group_count <= 40:
       k_2_count += cur_group_count
    elif 41 <= cur_group_count:
       ever_count += cur_group_count

musa_percent = musa_count / total_counter * 100
monbl_percent = monbl_count / total_counter * 100
kili_percent = kili_count / total_counter * 100
k_2_percent = k_2_count / total_counter * 100
ever_percent = ever_count / total_counter * 100


print(f"{musa_percent:.2f}%")
print(f"{monbl_percent:.2f}%")
print(f"{kili_percent:.2f}%")
print(f"{k_2_percent:.2f}%")
print(f"{ever_percent:.2f}%")
