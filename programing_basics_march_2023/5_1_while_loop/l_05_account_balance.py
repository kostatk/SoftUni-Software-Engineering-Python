account_balance = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    curr_amount = float(command)
    if curr_amount < 0:
        print("Invalid operation!")
        break
    account_balance += curr_amount
    print(f"Increase: {curr_amount:.2f}")

print(f"Total: {account_balance:.2f}")