from math import floor, ceil

num_days = int(input())
food_left_kg = int(input())
dog_food_daily_kg = float(input())
cat_food_daily_kg = float(input())
turtle_food_daily_grams = float(input())

total_food_needed_kg = num_days * (dog_food_daily_kg + cat_food_daily_kg + turtle_food_daily_grams / 1000)
diff = abs(total_food_needed_kg - food_left_kg)

if food_left_kg >= total_food_needed_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed")