kozunaci_num = int(input())

top_baker = ""
top_baker_points = 0

for _ in range(kozunaci_num):
    baker_name = input()
    total_baker_points = 0
    while True:
        command = input()
        if command == "Stop":
            print(f"{baker_name} has {total_baker_points} points.")
            if total_baker_points > top_baker_points:
                top_baker = baker_name
                top_baker_points = total_baker_points
                print(f"{baker_name} is the new number 1!")
            break
        curr_grade = int(command)
        total_baker_points += curr_grade

print(f"{top_baker} won competition with {top_baker_points} points!")
