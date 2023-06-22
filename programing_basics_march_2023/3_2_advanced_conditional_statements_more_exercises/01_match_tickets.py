budget = float(input())
category = input()
num_fans = int(input())

price = 0
transportation_rate = 0

if category == "VIP":
    price += 499.99 * num_fans
elif category == "Normal":
    price += 249.99 * num_fans

if 1 <= num_fans <= 4:
    transportation_rate += 0.75
elif 5 <= num_fans <= 9:
    transportation_rate += 0.60
elif 10 <= num_fans <= 24:
    transportation_rate += 0.50
elif 25 <= num_fans <= 49:
    transportation_rate += 0.40
elif 50 <= num_fans:
    transportation_rate += 0.25

remaining = budget * (1 - transportation_rate)

diff = abs(remaining - price)

if remaining >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")