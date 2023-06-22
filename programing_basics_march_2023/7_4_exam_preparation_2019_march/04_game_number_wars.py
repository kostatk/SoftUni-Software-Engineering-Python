player_one = input()
player_two = input()

points_one = 0
points_two = 0
IS_THERE_WAR = False

while True:
    command = input()
    if command == "End of game":
        print(f"{player_one} has {points_one} points")
        print(f"{player_two} has {points_two} points")
        break
    p_one_curr_card = int(command)
    p_two_curr_card = int(input())
    curr_diff = abs(p_one_curr_card - p_two_curr_card)
    if IS_THERE_WAR:
        print("Number wars!")
        if p_one_curr_card > p_two_curr_card:
            print(f"{player_one} is winner with {points_one} points")
            break
        elif p_one_curr_card < p_two_curr_card:
            print(f"{player_two} is winner with {points_two} points")
            break
    if p_one_curr_card == p_two_curr_card:
        IS_THERE_WAR = True
        continue
    if p_one_curr_card > p_two_curr_card:
        points_one += curr_diff
    elif p_one_curr_card < p_two_curr_card:
        points_two += curr_diff
