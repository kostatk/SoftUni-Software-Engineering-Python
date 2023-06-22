input_line = input()

my_list = input_line.split(", ")

index = -1
sheep_index = 1

if my_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    while True:
        index -= 1
        if my_list[index] == "wolf":
            break
        sheep_index += 1
    print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")
