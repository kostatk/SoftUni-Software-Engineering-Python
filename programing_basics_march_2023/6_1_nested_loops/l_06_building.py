floors = int(input())
rooms_per_floor = int(input())

for fl in range(floors, 0, -1):
    for room in range(rooms_per_floor):
        if fl == floors:
            cur_room_name = f"L{fl}{room}"
        else:
            if fl % 2 == 0:
                cur_room_name = f"O{fl}{room}"
            else:
                cur_room_name = f"A{fl}{room}"
        print(cur_room_name, end=" ")
    print()
