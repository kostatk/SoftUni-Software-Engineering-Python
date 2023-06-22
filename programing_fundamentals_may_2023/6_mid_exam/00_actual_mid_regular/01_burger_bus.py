
number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    income_of_owner = float(input())
    expenses_of_owner = float(input())
    if city % 5 == 0:
        income_of_owner *= 0.9
    elif city % 3 == 0:
        expenses_of_owner *= 1.5
    daily_profit = income_of_owner - expenses_of_owner
    print(f"In {city_name} Burger Bus earned {daily_profit:.2f} leva.")
    total_profit += daily_profit

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

