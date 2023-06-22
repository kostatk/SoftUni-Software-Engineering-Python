kilometers = int(input())
day_or_night = input()

price_with_taxi = 0
price_with_bus = 0.09 * kilometers
price_with_train = 0.06 * kilometers

if day_or_night == "day":
    price_with_taxi += 0.70 + 0.79 * kilometers
else:
    price_with_taxi += 0.70 + 0.90 * kilometers

if kilometers < 20:
    print(f"{price_with_taxi:.2f}")
elif kilometers < 100:
    print(f"{price_with_bus:.2f}")
else:
    print(f"{price_with_train:.2f}")
