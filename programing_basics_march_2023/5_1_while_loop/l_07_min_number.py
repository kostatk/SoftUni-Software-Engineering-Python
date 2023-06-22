from sys import maxsize

min_number = maxsize

while True:
    command = input()
    if command == "Stop":
        break
    curr_number = int(command)
    if curr_number < min_number:
        min_number = curr_number

print(min_number)