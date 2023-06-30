contract_term = input()
contract_type = input()
internet_addition = input()
months = int(input())

monthly_fee = 0

if contract_term == "one":
    if contract_type == "Small":
        monthly_fee = 9.98
    elif contract_type == "Middle":
        monthly_fee = 18.99
    elif contract_type == "Large":
        monthly_fee = 25.98
    elif contract_type == "ExtraLarge":
        monthly_fee = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        monthly_fee = 8.58
    elif contract_type == "Middle":
        monthly_fee = 17.09
    elif contract_type == "Large":
        monthly_fee = 23.59
    elif contract_type == "ExtraLarge":
        monthly_fee = 31.79

if internet_addition == "yes":
    if monthly_fee <= 10:
        monthly_fee += 5.50
    elif monthly_fee <= 30:
        monthly_fee += 4.35
    else:
        monthly_fee += 3.85


amount_due = monthly_fee * months

if contract_term == "two":
    amount_due *= 0.9625

print(f"{amount_due:.2f} lv.")
