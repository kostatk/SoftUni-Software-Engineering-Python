goal_amount = int(input())

HAS_FAILED = False
total_donated = 0
total_in_cash = 0
cash_counter = 0
total_with_cards = 0
cards_counter = 0
counter = 0

while total_donated < goal_amount:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        HAS_FAILED = True
        break
    curr_transaction = int(command)
    counter += 1
    if counter % 2 != 0 and curr_transaction <= 100:
        total_in_cash += curr_transaction
        cash_counter += 1
        total_donated += curr_transaction
        print("Product sold!")
    elif counter % 2 == 0 and curr_transaction >= 10:
        total_with_cards += curr_transaction
        cards_counter += 1
        total_donated += curr_transaction
        print("Product sold!")
    else:
        print("Error in transaction!")

if not HAS_FAILED:
    print(f"Average CS: {total_in_cash / cash_counter:.2f}")
    print(f"Average CC: {total_with_cards / cards_counter:.2f}")
