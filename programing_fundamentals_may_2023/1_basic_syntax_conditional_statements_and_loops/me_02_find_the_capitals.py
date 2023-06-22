word = input()

list_of_capitals = []

for character in range(len(word)):
    if 65 <= ord(word[character]) <= 90:
        list_of_capitals.append(character)

print(list_of_capitals)
