command = input()
to_do_list = []

while command != "End":
    to_do_list.append(command)
    command = input()

sorted_notes = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
return_notes = [command.split("-")[1] for command in to_do_list]

# print(to_do_list)
# print(sorted_notes)
print(return_notes)
