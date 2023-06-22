number_of_inputs = int(input())
are_balanced = True
last_bracket = ""

for commands in range(number_of_inputs):
    current_command = input()
    if (current_command == ")" and last_bracket != "(") or (current_command == "(" and last_bracket == "("):
        are_balanced = False
        break
    elif current_command == "(":
        last_bracket = "("
    elif current_command == ")":
        last_bracket = ""

if are_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
