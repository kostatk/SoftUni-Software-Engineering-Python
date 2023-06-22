final_word = ""
while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for ch in range(len(command)):
        final_word += command[ch] + command[ch]
    print(final_word)
    final_word = ""
