veggs_price_per_kg = float(input())
fruits_price_per_kg = float(input())
veggs_kilos = int(input())
fruits_kilos = int(input())

total_income_in_bgn = veggs_kilos * veggs_price_per_kg + fruits_kilos * fruits_price_per_kg

total_income_in_eur = total_income_in_bgn / 1.94

print(f"{total_income_in_eur:.2f}")

