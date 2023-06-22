purchased_food = int(input())

eaten_food = 0

while True:
    command = input()
    if command == "Adopted":
        break
    eaten_food += int(command)

purchased_food_in_grams = purchased_food * 1000
diff = abs(eaten_food - purchased_food_in_grams)

if eaten_food <= purchased_food_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams." )
else:
    print(f"Food is not enough. You need {diff} grams more.")
