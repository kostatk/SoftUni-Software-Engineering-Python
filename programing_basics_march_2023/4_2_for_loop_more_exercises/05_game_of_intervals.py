num_moves = int(input())

result = 0
int_1_perc = 0
int_2_perc = 0
int_3_perc = 0
int_4_perc = 0
int_5_perc = 0
int_6_perc = 0

percent_per_move = 100 / num_moves

for _ in range(num_moves):
    curr_number = int(input())
    if 0 <= curr_number <= 9:
        result += 0.2 * curr_number
        int_1_perc += percent_per_move
    elif 10 <= curr_number <= 19:
        result += 0.3 * curr_number
        int_2_perc += percent_per_move
    elif 20 <= curr_number <= 29:
        result += 0.4 * curr_number
        int_3_perc += percent_per_move
    elif 30 <= curr_number <= 39:
        result += 50
        int_4_perc += percent_per_move
    elif 40 <= curr_number <= 50:
        result += 100
        int_5_perc += percent_per_move
    else:
        result /= 2
        int_6_perc += percent_per_move

print(f"{result:.2f}")
print(f"From 0 to 9: {int_1_perc:.2f}%")
print(f"From 10 to 19: {int_2_perc:.2f}%")
print(f"From 20 to 29: {int_3_perc:.2f}%")
print(f"From 30 to 39: {int_4_perc:.2f}%")
print(f"From 40 to 50: {int_5_perc:.2f}%")
print(f"Invalid numbers: {int_6_perc:.2f}%")
