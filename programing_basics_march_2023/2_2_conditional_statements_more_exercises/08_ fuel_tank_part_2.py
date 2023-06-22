fuel_type = input()
quantity_litres = float(input())
is_there_card = input()

amount_for_fuel = 0
discount_per_quantity = 0
discount_for_type = 0

if is_there_card == "Yes":
    if fuel_type == "Gas":
        discount_for_type += 0.08
    elif fuel_type == "Gasoline":
        discount_for_type += 0.18
    elif fuel_type == "Diesel":
        discount_for_type += 0.12

if fuel_type == "Gas":
    amount_for_fuel += (0.93 - discount_for_type) * quantity_litres
elif fuel_type == "Gasoline":
    amount_for_fuel += (2.22 - discount_for_type) * quantity_litres
elif fuel_type == "Diesel":
    amount_for_fuel += (2.33 - discount_for_type) * quantity_litres

if quantity_litres > 25:
    discount_per_quantity += 0.1
elif quantity_litres > 20:
    discount_per_quantity += 0.08

amount_for_fuel *= 1 - discount_per_quantity

print(f"{amount_for_fuel:.2f} lv.")