fuel_type = input()
fuel_remaining = float(input())

if fuel_type == "Diesel":
    if fuel_remaining >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if fuel_remaining >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if fuel_remaining >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")