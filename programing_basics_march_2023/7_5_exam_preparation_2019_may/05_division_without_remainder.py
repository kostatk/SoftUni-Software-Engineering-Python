number_of_figures = int(input())
percent_per_number = 100 / number_of_figures
no_reminder_by_two = 0
no_reminder_by_three = 0
no_reminder_by_four = 0

for numbers in range(number_of_figures):
    current_number = int(input())
    if current_number % 2 == 0:
        no_reminder_by_two += percent_per_number
    if current_number % 3 == 0:
        no_reminder_by_three += percent_per_number
    if current_number % 4 == 0:
        no_reminder_by_four += percent_per_number

print(f"{no_reminder_by_two:.2f}%")
print(f"{no_reminder_by_three:.2f}%")
print(f"{no_reminder_by_four:.2f}%")