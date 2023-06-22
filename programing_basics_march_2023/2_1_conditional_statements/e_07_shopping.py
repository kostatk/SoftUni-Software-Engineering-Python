peter_budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())
discount = 0

total_amount_needed = (number_of_videocards * 250) + (number_of_processors * (number_of_videocards * 250 * 0.35)) + \
                      (number_of_ram * (number_of_videocards * 250 * 0.10))

if number_of_videocards > number_of_processors:
    discount = total_amount_needed * 0.15
    total_amount_needed = total_amount_needed - discount

difference = abs(peter_budget - total_amount_needed)
if peter_budget >= total_amount_needed:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")





