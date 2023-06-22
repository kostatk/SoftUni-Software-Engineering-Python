player = input()

remaining_points = 301
success_shots = 0
wrong_shots = 0

while True:
    sector = input()
    if sector == "Retire":
        print(f"{player} retired after {wrong_shots} unsuccessful shots.")
        break
    curr_points = int(input())
    if sector == "Single":
        curr_points = curr_points
    elif sector == "Double":
        curr_points = curr_points * 2
    elif sector == "Triple":
        curr_points = curr_points * 3
    if curr_points > remaining_points:
        wrong_shots += 1
    else:
        success_shots += 1
        remaining_points -= curr_points
    if remaining_points == 0:
        print(f"{player} won the leg with {success_shots} shots.")
        break
