
def is_number_perfect(number):
    sum_of_proper_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_proper_divisors += num
    if sum_of_proper_divisors == number:
        return True
    return False


user_number = int(input())
if is_number_perfect(user_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

