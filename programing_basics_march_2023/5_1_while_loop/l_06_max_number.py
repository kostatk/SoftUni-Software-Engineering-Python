from sys import maxsize

command = input()

max_number = -maxsize

while command != "Stop":
    curr_number = int(command)
    if curr_number > max_number:
        max_number = curr_number

    command = input()

print(max_number)