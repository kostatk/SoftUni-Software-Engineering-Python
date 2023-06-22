tournament_days = int(input())

money_collected = 0
winner_days = 0
win_counter_per_day = 0
lose_counter_per_day = 0
money_for_the_day = 0

for day in range(tournament_days):
    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            win_counter_per_day += 1
            money_for_the_day += 20
        elif result == "lose":
            lose_counter_per_day += 1

    if win_counter_per_day > lose_counter_per_day:
        money_for_the_day *= 1.1
        winner_days +=1
    money_collected += money_for_the_day
    win_counter_per_day = 0
    lose_counter_per_day = 0
    money_for_the_day = 0

if winner_days > tournament_days / 2:
    money_collected *= 1.2
    print(f"You won the tournament! Total raised money: {money_collected:.2f}")
else:
    print(f'You lost the tournament! Total raised money: {money_collected:.2f}')

