budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    current_product_price = int(command)
    if budget < current_product_price:
        print("You went in overdraft!")
        break
    budget -= current_product_price

