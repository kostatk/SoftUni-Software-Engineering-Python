nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_for_work = int(input())

nylon_expenses = (nylon_needed + 2) * 1.50
paint_expenses = (paint_needed * 1.1) * 14.50
thinner_expenses = thinner_needed * 5.00
bags_expenses = 0.40
material_expenses = nylon_expenses + paint_expenses + thinner_expenses + bags_expenses
expenses_for_work = (material_expenses * 0.30) * hours_for_work
total_expenses = expenses_for_work + material_expenses

print(total_expenses)