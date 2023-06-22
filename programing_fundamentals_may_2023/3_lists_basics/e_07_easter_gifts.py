list_of_gifts = input().split()

# print(list_of_gifts)

while True:
    list_of_command = input().split()
    if list_of_command[0] == "No":
        break
    elif list_of_command[0] == "OutOfStock":
        for element in list_of_gifts:
            if element == list_of_command[1]:
                list_of_gifts[list_of_gifts.index(element)] = "None"
    elif list_of_command[0] == "Required" and 0 <= int(list_of_command[2]) < len(list_of_gifts):
        list_of_gifts[int(list_of_command[2])] = list_of_command[1]
    elif list_of_command[0] == "JustInCase":
        list_of_gifts[-1] = list_of_command[1]

# print(list_of_gifts)

count = list_of_gifts.count("None")
for rolls in range(count):
    list_of_gifts.remove("None")

# print(list_of_gifts)
print(" ".join(list_of_gifts))
