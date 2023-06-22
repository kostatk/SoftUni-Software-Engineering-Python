hall_rent = float(input())

cake_price = hall_rent * 0.2
drinks_price = cake_price * 0.55
animation_price = hall_rent / 3

money_needed = hall_rent + cake_price + drinks_price + animation_price

print(f"{money_needed}")
