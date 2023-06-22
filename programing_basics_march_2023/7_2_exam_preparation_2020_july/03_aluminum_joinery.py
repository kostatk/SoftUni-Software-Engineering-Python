joinery_number = int(input())
joinery_size = input()
delivery_type = input()

price = 0

if joinery_number < 10:
    print("Invalid order")
else:
    if joinery_size == "90X130":
        price = 110
        if joinery_number > 60:
            price *= 0.92
        elif joinery_number > 30:
            price *= 0.95
    elif joinery_size == "100X150":
        price = 140
        if joinery_number > 80:
            price *= 0.90
        elif joinery_number > 40:
            price *= 0.94
    elif joinery_size == "130X180":
        price = 190
        if joinery_number > 50:
            price *= 0.88
        elif joinery_number > 20:
            price *= 0.93
    elif joinery_size == "200X300":
        price = 250
        if joinery_number > 50:
            price *= 0.86
        elif joinery_number > 25:
            price *= 0.91

    total_price = price * joinery_number

    if delivery_type == "With delivery":
        total_price += 60

    if joinery_number > 99:
        total_price *= 0.96

    print(f"{total_price:.2f} BGN")
