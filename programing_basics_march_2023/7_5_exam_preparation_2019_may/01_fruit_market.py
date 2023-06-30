strawberry_price = float(input())
quantity_banana = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6
banana_price = raspberries_price * 0.2


money_needed = strawberry_price * quantity_strawberries + banana_price * quantity_banana \
               + oranges_price * quantity_oranges + raspberries_price * quantity_raspberries

print(f"{money_needed:.2f}")
