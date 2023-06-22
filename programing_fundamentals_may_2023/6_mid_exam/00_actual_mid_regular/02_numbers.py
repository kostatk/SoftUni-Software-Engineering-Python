number_sequence = input().split()


def adding(existing_list, item):
    existing_list.append(item)
    return existing_list


def removing(existing_list, item):
    if item in existing_list:
        existing_list.remove(item)
    return existing_list


def replacing(existing_list, old_item, new_item):
    if old_item in existing_list:
        index_of_existing_item = existing_list.index(old_item)
        existing_list.insert(index_of_existing_item + 1, new_item)
        existing_list.remove(old_item)
    return existing_list


def collapsing(existing_list, item):
    existing_list = list(map(int, existing_list))
    item = int(item)
    existing_list = [num for num in existing_list if num >= int(item)]
    return list(map(str, existing_list))


while True:
    action = input().split()
    if action[0] == "Finish":
        break
    elif action[0] == "Add":
        number_sequence = adding(number_sequence, action[1])
    elif action[0] == "Remove":
        number_sequence = removing(number_sequence, action[1])
    elif action[0] == "Replace":
        number_sequence = replacing(number_sequence, action[1], action[2])
    elif action[0] == "Collapse":
        number_sequence = collapsing(number_sequence, action[1])

print(" ".join(number_sequence))
