student_name = input()

IS_EXPELLED = False
finished_classes = 0
failed_exams = 0
sum_grades = 0

while True:

    if failed_exams == 2:
        IS_EXPELLED = True
        break
    if finished_classes == 12:
        break

    curr_grade = float(input())

    if curr_grade >= 4:
        finished_classes += 1
        sum_grades += curr_grade
    else:
        failed_exams += 1

if IS_EXPELLED:
    print(f"{student_name} has been excluded at {finished_classes + 1} grade")
else:
    print(f"{student_name} graduated. Average grade: {sum_grades / finished_classes:.2f}")
