
def collecting_item(inventory, item):
    if item not in inventory:
        inventory.append(item)

    return inventory


def dropping_item(inventory, item):
    if item in inventory:
        inventory.remove(command[1])

    return inventory


def combining_items(inventory, item):
    item_list = item.split(":")
    old_item = item_list[0]
    new_item = item_list[1]
    if old_item in inventory:
        index_for_new_item = int(inventory.index(old_item)) + 1
        inventory.insert(index_for_new_item, new_item)

    return inventory


def renewing_items(inventory, item):
    if item in inventory:
        index_of_item = inventory.index(item)
        inventory.append(inventory.pop(index_of_item))

    return inventory


inventory_journal = input().split(", ")
while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break
    elif command[0] == "Collect":
        inventory_journal = collecting_item(inventory_journal, command[1])
    elif command[0] == "Drop":
        inventory_journal = dropping_item(inventory_journal, command[1])
    elif command[0] == "Combine Items":
        inventory_journal = combining_items(inventory_journal, command[1])
    elif command[0] == "Renew":
        inventory_journal = renewing_items(inventory_journal, command[1])
print(", ".join(inventory_journal))
