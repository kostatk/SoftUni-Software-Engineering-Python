
def odd_and_even_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        current_digit = int(digit)
        if current_digit % 2 == 0:
            sum_of_even_digits += current_digit
        else:
            sum_of_odd_digits += current_digit

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


user_number = input()
print(odd_and_even_sum(user_number))

#  СТАВА И ТАКА ДОЛНАТА ЧАСТ
#     return sum_of_even_digits, sum_of_odd_digits
#
#
# user_number = input()
# even_digits, odd_digits = odd_and_even_sum(user_number)
# print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")
