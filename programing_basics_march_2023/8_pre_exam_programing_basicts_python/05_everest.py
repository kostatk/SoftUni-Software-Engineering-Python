altitude = 5364
goal = 8848

days = 1

while True:
    is_he_resting = input()
    if is_he_resting == "END":
        print("Failed!")
        print(f"{altitude}")
        break
    if is_he_resting == "Yes":
        days += 1
    if days > 5:
        print("Failed!")
        print(f"{altitude}")
        break
    curr_meters = int(input())
    altitude += curr_meters
    if altitude >= goal:
        print(f"Goal reached for {days} days!")
        break
