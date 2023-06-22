goal_height = int(input())

bar = goal_height - 30
jumps = 0
missed_jumps = 0

while True:
    curr_jump = int(input())
    jumps += 1
    if curr_jump > bar:
        if bar == goal_height:
            print(f"Tihomir succeeded, he jumped over {bar}cm after {jumps} jumps.")
            break
        bar += 5
        missed_jumps = 0
        continue
    if curr_jump <= bar:
        missed_jumps += 1
        if missed_jumps == 3:
            print(f"Tihomir failed at {bar}cm after {jumps} jumps.")
            break
