num_days = int(input())

doctors = 7
checked = 0
unchecked = 0

for day in range(1, num_days + 1):
    patients_for_the_day = int(input())
    if day % 3 == 0 and unchecked > checked:
        doctors += 1

    if doctors >= patients_for_the_day:
        checked += patients_for_the_day
    else:
        checked += doctors
        unchecked += patients_for_the_day - doctors

print(f"Treated patients: {checked}.")
print(f"Untreated patients: {unchecked}.")



