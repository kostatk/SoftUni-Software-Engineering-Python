first_result = input()
second_result = input()
third_result = input()

wins = 0
draws = 0
loses = 0

if int(first_result[0]) > int(first_result[2]):
    wins += 1
elif int(first_result[0]) == int(first_result[2]):
    draws += 1
elif int(first_result[0]) < int(first_result[2]):
    loses += 1

if int(second_result[0]) > int(second_result[2]):
    wins += 1
elif int(second_result[0]) == int(second_result[2]):
    draws += 1
elif int(second_result[0]) < int(second_result[2]):
    loses += 1

if int(third_result[0]) > int(third_result[2]):
    wins += 1
elif int(third_result[0]) == int(third_result[2]):
    draws += 1
elif int(third_result[0]) < int(third_result[2]):
    loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
