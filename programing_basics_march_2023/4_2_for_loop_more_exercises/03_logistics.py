num_freight = int(input())

price_per_ton = 0
grand_total_price = 0
grand_total_tons = 0
bus_count = 0
truck_count = 0
train_count = 0

for _ in range(num_freight):
    curr_freight_tons = int(input())
    if curr_freight_tons <= 3:
        price_per_ton = 200
        bus_count += curr_freight_tons
    elif 4 <= curr_freight_tons <= 11:
        price_per_ton = 175
        truck_count += curr_freight_tons
    elif 12 <= curr_freight_tons:
        price_per_ton = 120
        train_count += curr_freight_tons
    grand_total_price += price_per_ton * curr_freight_tons
    grand_total_tons += curr_freight_tons

average_price = grand_total_price / grand_total_tons
bus_percent = bus_count / grand_total_tons * 100
truck_percent = truck_count / grand_total_tons * 100
train_percent = train_count / grand_total_tons * 100

print(f"{average_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
