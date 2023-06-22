from math import ceil

guests = int(input())
budget = int(input())

kozunak_expences = (ceil(guests / 3)) * 4
eggs_expenses = guests * 2 * 0.45

total_expenses = kozunak_expences + eggs_expenses

diff = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f"Lyubo bought {ceil(guests / 3)} Easter bread and {guests * 2} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")

