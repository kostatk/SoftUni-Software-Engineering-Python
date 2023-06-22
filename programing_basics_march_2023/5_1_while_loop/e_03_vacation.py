needed_money = float(input())
account_balance = float(input())

spend_days_counter = 0
total_days_counter = 0
HAS_FAILED = False

while account_balance < needed_money:
    curr_transaction_type = input()
    curr_transaction_amount = float(input())
    total_days_counter += 1

    if curr_transaction_type == "spend":
        spend_days_counter += 1
        account_balance -= curr_transaction_amount
        if account_balance < 0:
            account_balance = 0

    elif curr_transaction_type == "save":
        spend_days_counter = 0
        account_balance += curr_transaction_amount

    if spend_days_counter == 5:
        HAS_FAILED = True
        break

if not HAS_FAILED:
    print(f"You saved the money for {total_days_counter} days.")
else:
    print("You can't save the money.")
    print(f"{total_days_counter}")
