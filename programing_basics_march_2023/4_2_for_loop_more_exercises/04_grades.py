num_students = int(input())

percent_per_student = 100 / num_students

total_grades = 0
poor_percent = 0
average_percent = 0
good_percent = 0
excellent_percent = 0

for _ in range(num_students):
    curr_grade = float(input())
    total_grades += curr_grade
    if 2 <= curr_grade <= 2.99:
        poor_percent += percent_per_student
    elif 3 <= curr_grade <= 3.99:
        average_percent += percent_per_student
    elif 4 <= curr_grade <= 4.99:
        good_percent += percent_per_student
    elif curr_grade >= 5:
        excellent_percent += percent_per_student

print(f"Top students: {excellent_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {average_percent:.2f}%")
print(f"Fail: {poor_percent:.2f}%")
print(f"Average: {(total_grades / num_students):.2f}")
