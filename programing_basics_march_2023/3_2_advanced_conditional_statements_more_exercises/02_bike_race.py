juniors = int(input())
seniors = int(input())
race_type = input()

total_income = 0

if race_type == "trail":
    total_income = 5.50 * juniors + 7 * seniors
elif race_type == "cross-country":
    total_income = 8 * juniors + 9.50 * seniors
    if (juniors + seniors) >= 50:
        total_income *= 0.75
elif race_type == "downhill":
    total_income = 12.25 * juniors + 13.75 * seniors
elif race_type == "road":
    total_income = 20 * juniors + 21.50 * seniors

donation = total_income * 0.95

print(f"{donation:.2f}")


