coffee_counter = 0

while True:
    command = input()
    if command == "END":
        if coffee_counter > 5:
            print("You need extra sleep")
        else:
            print(coffee_counter)
        break
    if command.lower() != "coding" and command.lower() != "dog" and command.lower() != "cat" and command.lower() != "movie":
        continue
    if command.isupper():
        coffee_counter += 2
    else:
        coffee_counter += 1

