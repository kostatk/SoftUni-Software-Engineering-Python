# number_of_persons = int(input())
# elevator_capacity = int(input())
# courses_performed = 0
#
# while number_of_persons >= elevator_capacity:
#     courses_performed += 1
#     number_of_persons -= elevator_capacity
# if number_of_persons != 0:
#     courses_performed += 1
#
# print(courses_performed)


number_of_persons = int(input())
elevator_capacity = int(input())

courses_performed = number_of_persons // elevator_capacity
if number_of_persons % elevator_capacity != 0:
    courses_performed += 1

print(courses_performed)



