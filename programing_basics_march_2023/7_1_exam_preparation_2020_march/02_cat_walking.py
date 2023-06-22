walking_per_day_in_min = int(input())
walks_per_day = int(input())
calorie_intake_per_day = int(input())

total_calories_burned = walks_per_day * walking_per_day_in_min * 5

if total_calories_burned >= (calorie_intake_per_day / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")
