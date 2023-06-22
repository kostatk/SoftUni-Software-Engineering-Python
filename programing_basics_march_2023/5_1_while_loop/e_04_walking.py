steps_performed = 0

while steps_performed < 10000:
    command = input()
    if command == "Going home":
        current_steps = int(input())
        steps_performed += current_steps
        break
    else:
        current_steps = int(command)
        steps_performed += current_steps

diff = abs(steps_performed - 10000)

if steps_performed >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")



