jury_number = int(input())

presentation_grades = 0
presentation_average = 0
presentation_counter = 0
all_grades = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break
    presentation_counter += 1
    for grade in range(jury_number):
        cur_grade = float(input())
        presentation_grades += cur_grade
    presentation_average = presentation_grades / jury_number
    print(f"{presentation_name} - {presentation_average:.2f}.")
    all_grades += presentation_grades
    presentation_grades = 0

all_average = all_grades / (presentation_counter * jury_number)
print(f"Student's final assessment is {all_average:.2f}.")
