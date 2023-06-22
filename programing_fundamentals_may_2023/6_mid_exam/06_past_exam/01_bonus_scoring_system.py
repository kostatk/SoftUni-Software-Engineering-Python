from math import ceil


def bonus_calculator():
    number_of_students = int(input())
    number_of_lectures = int(input())
    additional_bonus = int(input())
    max_bonus = 0
    attendances_of_student_with_max_bonus = 0

    for student in range(number_of_students):
        student_attendances = int(input())
        current_bonus = student_attendances / number_of_lectures * (5 + additional_bonus)
        if current_bonus > max_bonus:
            max_bonus = current_bonus
            attendances_of_student_with_max_bonus = student_attendances

    return max_bonus, attendances_of_student_with_max_bonus


max_bonus_final, attendances_final = bonus_calculator()

print(f"Max Bonus: {ceil(max_bonus_final)}.")
print(f"The student has attended {attendances_final} lectures.")
