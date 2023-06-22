guests = int(input())
price = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price *= 0.85
elif 15 < guests <= 20:
    price *= 0.80
elif 20 < guests:
    price *= 0.75

total_expenses = price * guests + budget * 0.1

diff = abs(total_expenses - budget)

if total_expenses <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
