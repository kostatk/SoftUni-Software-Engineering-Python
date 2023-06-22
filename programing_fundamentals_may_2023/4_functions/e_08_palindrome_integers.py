
def check_palindrome(number):
    if number == number[::-1]:
        return True
    return False


list_of_strings = input().split(", ")
for element in list_of_strings:
    print(check_palindrome(element))


# LONG AND HARD VERSION
# def check_palindrome(number):
#     if len(number) == 1:
#         print("True")
#     else:
#         is_true = True
#         for index in range(0, len(number) // 2):
#             if number[index] != number[-1 - index]:
#                 is_true = False
#                 break
#         if is_true:
#             print("True")
#         else:
#             print("False")
#
#
# list_of_strings = input().split(", ")
# for element in list_of_strings:
#     check_palindrome(element)
#
#
#
