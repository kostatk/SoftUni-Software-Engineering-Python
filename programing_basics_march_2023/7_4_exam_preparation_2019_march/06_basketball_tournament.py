total_tournaments = 0
wins = 0
loses = 0

while True:
    tournament = input()
    if tournament == "End of tournaments":
        print(f"{wins / total_tournaments * 100:.2f}% matches win")
        print(f"{loses / total_tournaments * 100:.2f}% matches lost")
        break
    games = int(input())
    for g in range(1, games + 1):
        total_tournaments += 1
        d_team_points = int(input())
        other_team_points = int(input())
        diff = abs(d_team_points - other_team_points)
        if d_team_points > other_team_points:
            print(f"Game {g} of tournament {tournament}: win with {diff} points.")
            wins += 1
        elif d_team_points < other_team_points:
            print(f"Game {g} of tournament {tournament}: lost with {diff} points.")
            loses += 1
