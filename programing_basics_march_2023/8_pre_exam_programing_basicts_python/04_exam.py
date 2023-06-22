num_students = int(input())

percent_per_one = 100 / num_students
total_grades = 0

top_students = 0
good_students = 0
ok_students = 0
fail_students = 0

for _ in range(num_students):
    curr_grade = float(input())
    total_grades += curr_grade
    if 5 <= curr_grade:
        top_students += percent_per_one
    elif 4 <= curr_grade <= 4.99:
        good_students += percent_per_one
    elif 3 <= curr_grade <= 3.99:
        ok_students += percent_per_one
    elif curr_grade < 3:
        fail_students += percent_per_one

average_grade = total_grades / num_students

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {good_students:.2f}%")
print(f"Between 3.00 and 3.99: {ok_students:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")
