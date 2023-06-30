budget = float(input())
product_counter = 0
money_spent = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {product_counter} products for {money_spent:.2f} leva.")
        break
    price = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        price *= 0.5
    if budget - money_spent >= price:
        money_spent += price
    else:
        print("You don't have enough money!")
        print(f"You need {abs(budget - money_spent - price):.2f} leva!")
        break

