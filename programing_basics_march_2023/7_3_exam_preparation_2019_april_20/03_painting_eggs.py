size = input()
colour = input()
number = int(input())

price = 0

if size == "Large":
    if colour == "Red":
        price = 16
    elif colour == "Green":
        price = 12
    elif colour == "Yellow":
        price = 9
elif size == "Medium":
    if colour == "Red":
        price = 13
    elif colour == "Green":
        price = 9
    elif colour == "Yellow":
        price = 7
elif size == "Small":
    if colour == "Red":
        price = 9
    elif colour == "Green":
        price = 8
    elif colour == "Yellow":
        price = 5

end_price = price * number * 0.65

print(f"{end_price:.2f} leva.")
