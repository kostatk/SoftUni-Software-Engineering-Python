clients_number = int(input())

total_spend = 0

for client in range(clients_number):
    curr_price = 0
    curr_purchase_counter = 0
    while True:
        curr_purchase = input()
        if curr_purchase == "Finish":
            if curr_purchase_counter % 2 == 0:
                curr_price *= 0.8
            print(f"You purchased {curr_purchase_counter} items for {curr_price:.2f} leva.")
            break
        curr_purchase_counter += 1
        if curr_purchase == "basket":
            curr_price += 1.50
        elif curr_purchase == "wreath":
            curr_price += 3.80
        elif curr_purchase == "chocolate bunny":
            curr_price += 7
    total_spend += curr_price

average_spend = total_spend / clients_number
print(f"Average bill per client is: {average_spend:.2f} leva.")
