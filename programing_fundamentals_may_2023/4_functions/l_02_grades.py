
def grade_checker(grade):
    grade_in_words = ""
    if 2.00 <= grade <= 2.99:
        grade_in_words = "Fail"
    elif 3.00 <= grade <= 3.49:
        grade_in_words = "Poor"
    elif 3.50 <= grade <= 4.49:
        grade_in_words = "Good"
    elif 4.50 <= grade <= 5.49:
        grade_in_words = "Very Good"
    elif 5.50 <= grade <= 6.00:
        grade_in_words = "Excellent"

    return grade_in_words


user_grade = float(input())
print(grade_checker(user_grade))
