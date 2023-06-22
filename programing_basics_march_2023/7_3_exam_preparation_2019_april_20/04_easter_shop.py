eggs_at_beginning = int(input())

sold_eggs = 0

while True:
    command = input()
    if command == "Close":
        print(f"Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break
    curr_eggs = int(input())
    if command == "Buy":
        if curr_eggs > eggs_at_beginning:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_at_beginning}.")
            break
        eggs_at_beginning -= curr_eggs
        sold_eggs += curr_eggs
    elif command == "Fill":
        eggs_at_beginning += curr_eggs
