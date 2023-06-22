unsatisfactory_grades_limit = int(input())

unsatisfactory_grades_counter = 0
task_counter = 0
total_grades = 0
last_task = ""

while True:
    command = input()
    if command == "Enough":
        average_grade = total_grades / task_counter
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {task_counter}")
        print(f"Last problem: {last_task}")
        break

    curr_grade = int(input())

    if curr_grade <= 4:
        unsatisfactory_grades_counter += 1

    if unsatisfactory_grades_counter == unsatisfactory_grades_limit:
        print(f"You need a break, {unsatisfactory_grades_counter} poor grades.")
        break

    task_counter += 1
    total_grades += curr_grade
    last_task = command
