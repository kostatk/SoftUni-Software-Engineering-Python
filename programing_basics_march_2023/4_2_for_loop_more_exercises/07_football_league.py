stadium_capacity = int(input())
fan_number = int(input())

percent_per_fan = 100 / fan_number
percent_occupancy = fan_number / stadium_capacity * 100

a_percent = 0
b_percent = 0
v_percent = 0
g_percent = 0

for _ in range(fan_number):
    curr_sector = input()
    if curr_sector == "A":
        a_percent += percent_per_fan
    elif curr_sector == "B":
        b_percent += percent_per_fan
    elif curr_sector == "V":
        v_percent += percent_per_fan
    elif curr_sector == "G":
        g_percent += percent_per_fan

print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{percent_occupancy:.2f}%")
