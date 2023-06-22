dishwasher_bottles = int(input())

# бутилка съдържа 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.

available_dishwasher_in_ml = dishwasher_bottles * 750

washes_counter = 0
cleaned_dishes = 0
cleaned_pots = 0
dishwasher_needed = 0
STOPPED = False

while True:
    if dishwasher_needed >= available_dishwasher_in_ml:
        break
    command = input()
    if command == "End":
        STOPPED = True
        break
    curr_dishes = int(command)
    washes_counter += 1
    if washes_counter % 3 == 0:
        cleaned_pots += curr_dishes
        dishwasher_needed += curr_dishes * 15
    else:
        cleaned_dishes += curr_dishes
        dishwasher_needed += curr_dishes * 5

diff = abs(available_dishwasher_in_ml - dishwasher_needed)

if STOPPED:
    print(f"Detergent was enough!")
    print(f"{cleaned_dishes} dishes and {cleaned_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
