budget = float(input())
season = input()

class_car = ""
type_car = ""
price = budget

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price *= 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price *= 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price *= 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price *= 0.80
else:
    class_car = "Luxury class"
    type_car = "Jeep"
    price *= 0.90

print(class_car)
print(f"{type_car} - {price:.2f}")