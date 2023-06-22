# Това е решение с въртене през къщите като ако има 4 къщи ги обикаля 1 2 3 4 1 2 3 4 1 2 3 4

neighborhood = [int(item) for item in input().split("@")]
current_index = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break
    current_index += int(command[1])

    if current_index >= len(neighborhood):
        current_index = 0

    if neighborhood[current_index] != 0:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    else:
        print(f"Place {current_index} already had Valentine's day.")

print(f"Cupid's last position was {current_index}.")
checked_houses = neighborhood.count(0)
if checked_houses == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - checked_houses} places.")
