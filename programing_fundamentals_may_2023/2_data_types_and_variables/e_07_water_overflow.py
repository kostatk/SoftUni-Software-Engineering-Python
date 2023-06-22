number_of_pours = int(input())

tank_capacity_remaining = 255
poured_water = 0

for pours in range(number_of_pours):
    current_liters_of_pour = int(input())
    if current_liters_of_pour > tank_capacity_remaining:
        print("Insufficient capacity!")
        continue
    tank_capacity_remaining -= current_liters_of_pour
    poured_water += current_liters_of_pour

print(poured_water)
