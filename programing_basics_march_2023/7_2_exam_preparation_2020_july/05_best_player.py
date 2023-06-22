
best_player = ""
goals = 0

while True:
    name = input()
    if name == "END":
        break
    cur_goals = int(input())
    if cur_goals > goals:
        goals = cur_goals
        best_player = name
    if goals >= 10:
        break

print(f"{best_player} is the best player!")
if goals >= 3:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")

