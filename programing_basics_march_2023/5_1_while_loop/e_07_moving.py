place_width = int(input())
place_length = int(input())
place_height = int(input())

free_space = place_width * place_length * place_height

place_taken = 0
HE_IS_DONE = False

while True:
    command = input()
    if command == "Done":
        HE_IS_DONE = True
        break
    curr_boxes = int(command)
    place_taken += curr_boxes
    if place_taken > free_space:
        break

if HE_IS_DONE:
    print(f"{free_space - place_taken} Cubic meters left.")
else:
    print(f"No more free space! You need {place_taken - free_space} Cubic meters more.")
