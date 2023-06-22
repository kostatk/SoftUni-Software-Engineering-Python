budget = int(input())
season = input()
num_fishermen = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Summer" or season == "Autumn":
    total_price = 4200
elif season == "Winter":
    total_price = 2600

if num_fishermen <= 6:
    total_price *= 0.9
    if num_fishermen % 2 == 0 and season != "Autumn":
        total_price *= 0.95
elif 6 < num_fishermen <= 11:
    total_price *= 0.85
    if num_fishermen % 2 == 0 and season != "Autumn":
        total_price *= 0.95
elif num_fishermen >= 12:
    total_price *= 0.75
    if num_fishermen % 2 == 0 and season != "Autumn":
        total_price *= 0.95

# В стремежа си да използвам вложена условна конструцкия, напълно излишно съм повторил един и същи код 3 пъти
# Съвсем спокойно следното може да е нова IF конструкция и да е само веднъж изписано
# if num_fishermen % 2 == 0 and season != "Autumn":
#         total_price *= 0.95

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")