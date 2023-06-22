cards = input()
list_of_sent_players = cards.split(" ")

list_team_a = []
list_team_b = []
is_terminated = False

for number in range(1, 12):
    list_team_a.append("A-" + str(number))
    list_team_b.append("B-" + str(number))

for player in list_of_sent_players:
    if player in list_team_a:
        list_team_a.remove(player)
    elif player in list_team_b:
        list_team_b.remove(player)
    if len(list_team_a) < 7 or len(list_team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
if is_terminated:
    print("Game was terminated")
