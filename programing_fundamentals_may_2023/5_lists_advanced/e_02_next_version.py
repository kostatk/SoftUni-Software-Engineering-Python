
current_version = [int(digit) for digit in input().split(".")]

for index in range(-1, -len(current_version) - 1, -1):
    if current_version[index] != 9:
        current_version[index] += 1
        break
    else:
        current_version[index] = 0

list_to_print = map(str, current_version)

print(".".join(list_to_print))

# "{n1}.{n2}.{n3}"
