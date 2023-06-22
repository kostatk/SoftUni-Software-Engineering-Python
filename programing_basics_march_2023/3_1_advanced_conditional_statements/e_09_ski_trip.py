days = int(input())
room_type = input()
feedback = input()

price = 0
discount = 0

if room_type == "room for one person":
    price += 18
elif room_type == "apartment":
    if days < 10:
        discount += 0.3
    elif 10 <= days <= 15:
        discount += 0.35
    else:
        discount += 0.5
    price += 25 * (1 - discount)
elif room_type == "president apartment":
    if days < 10:
        discount += 0.1
    elif 10 <= days <= 15:
        discount += 0.15
    else:
        discount += 0.2
    price += 35 * (1 - discount)

total_price = price * (days - 1)

if feedback == "positive":
    total_price *= 1.25
elif feedback == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")
