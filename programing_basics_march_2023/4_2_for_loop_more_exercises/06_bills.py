months = int(input())

total_electricity = 0
total_others = 0
total_bills = 0

for _ in range(months):
    curr_electricity = float(input())
    total_electricity += curr_electricity
    total_others += (curr_electricity + 20 + 15) * 1.2
    total_bills += (curr_electricity + 20 + 15) * 2.2

average_bills = total_bills / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {months * 20:.2f} lv")
print(f"Internet: {months * 15:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_bills:.2f} lv")
