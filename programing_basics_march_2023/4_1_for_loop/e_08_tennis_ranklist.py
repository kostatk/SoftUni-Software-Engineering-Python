from math import floor

num_games = int(input())
total_points = int(input())

game_points = 0
wins_counter = 0

for _ in range(num_games):
    place = input()
    if place == "W":
        game_points += 2000
        wins_counter += 1
    elif place == "F":
        game_points += 1200
    elif place == "SF":
        game_points += 720

print(f"Final points: {total_points + game_points}")
print(f"Average points: {floor(game_points / num_games)}") # вместо floor можем да използваме целочислено делене //
print(f"{wins_counter / num_games * 100:.2f}%")
