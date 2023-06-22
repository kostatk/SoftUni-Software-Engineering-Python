
initial_energy = 100
initial_coins = 100
work_day_events = input().split("|")
is_finished = True

for event in work_day_events:
    action, number = event.split("-")
    value = int(number)
    if action == "rest":
        if value + initial_energy > 100:
            value = 100 - initial_energy
        initial_energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {initial_energy}.")
    elif action == "order":
        if initial_energy >= 30:
            initial_coins += value
            initial_energy -= 30
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= value:
            initial_coins -= value
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_finished = False
            break

if is_finished:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")


