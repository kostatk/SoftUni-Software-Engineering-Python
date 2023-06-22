
def urgent_product(existing_list, product):
    if product not in existing_list:
        existing_list.insert(0, product)
    return existing_list


def unnecessary_product(existing_list, product):
    if product in existing_list:
        existing_list.remove(product)
    return existing_list


def correction(existing_list, old_product, new_product):
    if old_product in existing_list:
        existing_list[existing_list.index(old_product)] = new_product
    return existing_list


def rearrange(existing_list, product):
    if product in existing_list:
        existing_list.append(existing_list.pop(existing_list.index(product)))
    return existing_list


grocery_list = input().split("!")
while True:
    command = input().split()
    if command[0] == "Go":
        break
    if command[0] == "Urgent":
        grocery_list = urgent_product(grocery_list, command[1])
    elif command[0] == "Unnecessary":
        grocery_list = unnecessary_product(grocery_list, command[1])
    elif command[0] == "Correct":
        grocery_list = correction(grocery_list, command[1], command[2])
    elif command[0] == "Rearrange":
        grocery_list = rearrange(grocery_list, command[1])
print(", ".join(grocery_list))


