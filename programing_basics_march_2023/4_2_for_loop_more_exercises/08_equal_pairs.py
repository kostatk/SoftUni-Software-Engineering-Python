num_pairs = int(input())

previous_sum = 0
max_diff = 0

for i in range(num_pairs):
    first_num = int(input())
    second_num = int(input())
    if i > 0:
        max_diff = abs((first_num + second_num) - previous_sum)
    previous_sum = first_num + second_num

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")
