train_list = [0] * int(input())

while True:
    command = input().split()
    if command[0] == 'End':
        print(train_list)
        break
    elif command[0] == 'add':
        train_list[-1] += int(command[1])
    elif command[0] == 'insert':
        train_list[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        train_list[int(command[1])] -= int(command[2])
