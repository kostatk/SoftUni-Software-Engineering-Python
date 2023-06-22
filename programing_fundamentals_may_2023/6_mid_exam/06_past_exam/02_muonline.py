
def potion_healing(room_list, health):
    healing_amount = int(room_list[1])
    if health + healing_amount <= 100:
        health += healing_amount
    else:
        healing_amount = 100 - health
        health = 100
    print(f"You healed for {healing_amount} hp.")
    print(f"Current health: {health} hp.")

    return health


def bitcoins_find(room_list, bitcoins):
    bitcoins_found = int(room_list[1])
    bitcoins += bitcoins_found
    print(f"You found {bitcoins_found} bitcoins.")

    return bitcoins


def meeting_monster(room_list, health):
    death_occur = False
    attack_power = int(room_list[1])
    monster = room_list[0]
    if health - attack_power > 0:
        health -= attack_power
        print(f"You slayed {monster}.")
    else:
        death_occur = True
        print(f"You died! Killed by {monster}.")

    return health, death_occur


current_health = 100
current_bitcoins = 0
list_of_rooms = input().split("|")
is_dead = False
best_room = 0

for room in list_of_rooms:
    best_room += 1
    current_room_list = room.split()
    if current_room_list[0] == "potion":
        current_health = potion_healing(current_room_list, current_health)
    elif current_room_list[0] == "chest":
        current_bitcoins = bitcoins_find(current_room_list, current_bitcoins)
    else:
        current_health, is_dead = meeting_monster(current_room_list, current_health)
    if is_dead:
        print(f"Best room: {best_room}")
        break

if not is_dead:
    print(f"You've made it!\nBitcoins: {current_bitcoins}\nHealth: {current_health}")
