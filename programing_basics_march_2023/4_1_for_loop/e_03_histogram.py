# n = int(input())
#
# # percent_per_number = 100 / n
#
# p_1 = 0
# p_2 = 0
# p_3 = 0
# p_4 = 0
# p_5 = 0
#
# for _ in range(n):
#     curr_num = int(input())
#     if curr_num < 200:
#         p_1 += 1
#     elif 200 <= curr_num <= 399:
#         p_2 += 1
#     elif 400 <= curr_num <= 599:
#         p_3 += 1
#     elif 600 <= curr_num <= 799:
#         p_4 += 1
#     elif curr_num >= 800:
#         p_5 += 1
#
# p_1_percent = p_1 / n * 100
# p_2_percent = p_2 / n * 100
# p_3_percent = p_3 / n * 100
# p_4_percent = p_4 / n * 100
# p_5_percent = p_5 / n * 100
#
# print(f"{p_1_percent:.2f}%")
# print(f"{p_2_percent:.2f}%")
# print(f"{p_3_percent:.2f}%")
# print(f"{p_4_percent:.2f}%")
# print(f"{p_5_percent:.2f}%")

n = int(input())

percent_per_number = 100 / n

p_1_percent = 0
p_2_percent = 0
p_3_percent = 0
p_4_percent = 0
p_5_percent = 0

for _ in range(n):
    curr_num = int(input())
    if curr_num < 200:
        p_1_percent += percent_per_number
    elif 200 <= curr_num <= 399:
        p_2_percent += percent_per_number
    elif 400 <= curr_num <= 599:
        p_3_percent += percent_per_number
    elif 600 <= curr_num <= 799:
        p_4_percent += percent_per_number
    elif curr_num >= 800:
        p_5_percent += percent_per_number

print(f"{p_1_percent:.2f}%")
print(f"{p_2_percent:.2f}%")
print(f"{p_3_percent:.2f}%")
print(f"{p_4_percent:.2f}%")
print(f"{p_5_percent:.2f}%")

