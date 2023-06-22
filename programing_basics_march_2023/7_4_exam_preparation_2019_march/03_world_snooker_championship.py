stage = input()
ticket = input()
number_of_tickets = int(input())
photos = input()

price = 0

if stage == "Quarter final":
    if ticket == "Standard":
        price = 55.50
    elif ticket == "Premium":
        price = 105.20
    elif ticket == "VIP":
        price = 118.90
elif stage == "Semi final":
    if ticket == "Standard":
        price = 75.88
    elif ticket == "Premium":
        price = 125.22
    elif ticket == "VIP":
        price = 300.40
elif stage == "Final":
    if ticket == "Standard":
        price = 110.10
    elif ticket == "Premium":
        price = 160.66
    elif ticket == "VIP":
        price = 400

total_price = price * number_of_tickets

if total_price > 4000:
    total_price *= 0.75
elif total_price > 2500:
    total_price *= 0.90
    if photos == "Y":
        total_price += 40 * number_of_tickets
else:
    if photos == "Y":
        total_price += 40 * number_of_tickets

print(f"{total_price:.2f}")
