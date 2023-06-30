budget = float(input())
fuel_needed = float(input())
day = input()

fuel_price = 2.10
guide_price = 100
money_needed = 0
discount = 0
if day == "Saturday":
    discount = 0.1
elif day == "Sunday":
    discount = 0.2

money_needed = ((fuel_needed * fuel_price) + guide_price) * (1 - discount)
diff = abs(budget - money_needed)

if budget >= money_needed:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
