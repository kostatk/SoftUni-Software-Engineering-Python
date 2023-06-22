season = input()
km_per_month = float(input())

price_per_km = 0

if 10000 < km_per_month <= 20000:
    price_per_km = 1.45
else:
    if season == "Spring" or season == "Autumn":
        if km_per_month <= 5000:
            price_per_km = 0.75
        elif 5000 < km_per_month <= 10000:
            price_per_km = 0.95
    elif season == "Summer":
        if km_per_month <= 5000:
            price_per_km = 0.90
        elif 5000 < km_per_month <= 10000:
            price_per_km = 1.10
    elif season == "Winter":
        if km_per_month <= 5000:
            price_per_km = 1.05
        elif 5000 < km_per_month <= 10000:
            price_per_km = 1.25

final_income = price_per_km * km_per_month * 4 * 0.9

print(f"{final_income:.2f}")
