list_ot_times = input().split()

middle = len(list_ot_times) // 2

left_sum = 0
right_sum = 0

for index in range(middle):
    left_sum += int(list_ot_times[index])
    if list_ot_times[index] == "0":
        left_sum *= 0.8
for index in range(-1, middle - len(list_ot_times), -1):
    right_sum += int(list_ot_times[index])
    if list_ot_times[index] == "0":
        right_sum *= 0.8

if left_sum < right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_sum:.1f}")
