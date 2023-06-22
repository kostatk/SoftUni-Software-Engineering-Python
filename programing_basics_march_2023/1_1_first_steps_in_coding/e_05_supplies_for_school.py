pens_num = int(input())
markers_num = int(input())
cleaner_litres = int(input())
discount_percent = int(input())

amount_for_supplies = (pens_num * 5.80) + (markers_num * 7.20) + (cleaner_litres * 1.20)
discount_amount = amount_for_supplies * discount_percent / 100
amount_needed = amount_for_supplies - discount_amount

print(amount_needed)