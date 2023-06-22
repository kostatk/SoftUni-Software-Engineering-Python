actor_name = input()
academy_points = float(input())
num_appraisers = int(input())

nomination_points = 1250.50 # когато нещо го ползваме повече от веднъж е добре да го въведем в променлива

for _ in range(num_appraisers):
    apprais_name = input()
    apprais_points = float(input())
    academy_points += len(apprais_name) * apprais_points / 2

    if academy_points > nomination_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points <= nomination_points:
    needed_points = nomination_points - academy_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
