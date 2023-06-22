from math import floor

tournaments = int(input())
initial_points = int(input())

wins = 0
added_points = 0

for p in range(tournaments):
    curr_stage = input()
    if curr_stage == "W":
        added_points += 2000
        wins += 1
    elif curr_stage == "F":
        added_points += 1200
    elif curr_stage == "SF":
        added_points += 720

final_points = initial_points + added_points
average_points = added_points / tournaments
win_percent = wins / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percent:.2f}%")
