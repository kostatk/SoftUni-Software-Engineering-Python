days = int(input())
hours = int(input())
total_price = 0

for day in range(1, days + 1):
    day_price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_price += 1.25
        else:
            day_price += 1.00
    print(f"Day: {day} - {day_price:.2f} leva")
    total_price += day_price

print(f"Total: {total_price:.2f} leva")
