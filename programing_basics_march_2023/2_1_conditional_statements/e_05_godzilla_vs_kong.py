movie_budget = float(input())
num_extras = int(input())
clothes_price_per_extra = float(input())

clothes_sum = num_extras * clothes_price_per_extra
decor_sum = movie_budget * 0.1

if num_extras > 150:
    clothes_sum *= 0.9

total_amount_needed = clothes_sum + decor_sum
difference = abs(total_amount_needed - movie_budget)

if total_amount_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")