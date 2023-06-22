amount = float(input())
end_year = int(input())

age = 18
needed_amount = 0

for year in range(1800, end_year + 1):
    if year % 2 == 0:
        needed_amount += 12000
    else:
        needed_amount += 12000 + 50 * age
    age += 1
diff = abs(amount - needed_amount)

if amount >= needed_amount:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")