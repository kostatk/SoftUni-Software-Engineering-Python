fruit = input()
day = input()
quantity = float(input())

FALSE_INPUT = False
amount = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        amount = quantity * 2.50
    elif fruit == "apple":
        amount = quantity * 1.20
    elif fruit == "orange":
        amount = quantity * 0.85
    elif fruit == "grapefruit":
        amount = quantity * 1.45
    elif fruit == "kiwi":
        amount = quantity * 2.70
    elif fruit == "pineapple":
        amount = quantity * 5.50
    elif fruit == "grapes":
        amount = quantity * 3.85
    else:
        FALSE_INPUT = True
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        amount = quantity * 2.70
    elif fruit == "apple":
        amount = quantity * 1.25
    elif fruit == "orange":
        amount = quantity * 0.90
    elif fruit == "grapefruit":
        amount = quantity * 1.60
    elif fruit == "kiwi":
        amount = quantity * 3.00
    elif fruit == "pineapple":
        amount = quantity * 5.60
    elif fruit == "grapes":
        amount = quantity * 4.20
    else:
        FALSE_INPUT = True
else:
    FALSE_INPUT = True

if not FALSE_INPUT:
    print(f"{amount:.2f}")
else:
    print("error")
