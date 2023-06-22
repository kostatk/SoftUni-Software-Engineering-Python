
list_of_items = input().split("|")
initial_money = float(input())
remaining_money = initial_money
purchased_items_sell_prices = []

for item in list_of_items:
    current_item_list = item.split("->")
    item_type = current_item_list[0]
    item_price = float(current_item_list[1])
    if remaining_money >= item_price:
        if item_type == "Clothes" and item_price <= 50:
            remaining_money -= item_price
            purchased_items_sell_prices.append(item_price * 1.4)
        elif item_type == "Shoes" and item_price <= 35:
            remaining_money -= item_price
            purchased_items_sell_prices.append(item_price * 1.4)
        elif item_type == "Accessories" and item_price <= 20.50:
            remaining_money -= item_price
            purchased_items_sell_prices.append(item_price * 1.4)

for price in purchased_items_sell_prices:
    print(f"{price:.2f}", end=" ")
print()

# Това е с лист комприхеншън
# print(" ".join(f"{price:.2f}" for price in purchased_items_sell_prices))

profit = sum(purchased_items_sell_prices) - (initial_money - remaining_money)
print(f"Profit: {profit:.2f}")
if sum(purchased_items_sell_prices) + remaining_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")






