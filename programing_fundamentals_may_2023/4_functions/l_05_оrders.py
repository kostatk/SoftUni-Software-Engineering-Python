
def orders_bill(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return quantity * price


user_product = input()
user_quantity = int(input())
print(f"{orders_bill(user_product, user_quantity):.2f}")
