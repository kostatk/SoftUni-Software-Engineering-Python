# people_list = input().split()
# step_to_kill = int(input())
# initial_step_to_kill = step_to_kill
# step_back = 1
#
# for rolls in range(1, len(people_list) - 1):
#     index = step_to_kill - step_back
#
#
#     step_back += 1
#     step_to_kill += initial_step_to_kill
#     print(index)


people_numbers = input().split()
k_step = int(input())

people_killed = []
counter = 0
index = 0

while len(people_numbers) > 0:
    counter += 1
    if counter % k_step == 0:
        people_killed.append(people_numbers.pop(index))
    else:
        index += 1
    if index >= len(people_numbers):
        index = 0

print(str(people_killed).replace(' ', '').replace('\'', ''))
