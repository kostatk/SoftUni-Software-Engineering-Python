
number_of_rooms = int(input())

free_chairs_counter = 0
all_free = True

for room in range(1, number_of_rooms + 1):
    cur_room_list = input().split()
    free_chairs = len(cur_room_list[0])
    needed_chairs = int(cur_room_list[1])
    if free_chairs < needed_chairs:
        diff = needed_chairs - free_chairs
        print(f"{diff} more chairs needed in room {room}")
        all_free = False
    else:
        free_chairs_counter += free_chairs - needed_chairs

if all_free:
    print(f"Game On, {free_chairs_counter} free chairs left")
