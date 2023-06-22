cake_width = int(input())
cake_length = int(input())

total_pieces = cake_length * cake_width

total_pieces_taken = 0
ENOUGH = False

while total_pieces_taken < total_pieces:
    command = input()
    if command == "STOP":
        ENOUGH = True
        break

    curr_pieces_taken = int(command)
    total_pieces_taken += curr_pieces_taken

if ENOUGH:
    print(f"{total_pieces - total_pieces_taken} pieces are left.")
else:
    print(f"No more cake left! You need {total_pieces_taken - total_pieces} pieces more.")
