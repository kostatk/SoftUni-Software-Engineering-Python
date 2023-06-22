capacity = float(input())

suitcases_counter = 0

while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcases_counter += 1
    cur_suitcase = float(command)
    if suitcases_counter % 3 == 0:
        cur_suitcase *= 1.1
    capacity -= cur_suitcase
    if capacity < 0:
        print("No more space!")
        suitcases_counter -= 1
        break

print(f"Statistic: {suitcases_counter} suitcases loaded.")
