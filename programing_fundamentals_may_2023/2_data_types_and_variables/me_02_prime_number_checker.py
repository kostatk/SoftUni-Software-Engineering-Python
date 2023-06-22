number = int(input())
divisor_counter = 0
is_prime = False

if number >= 1:
    for divisor in range(2, number + 1):
        if number % divisor == 0:
            divisor_counter += 1
    if divisor_counter == 1:
        is_prime = True

print(is_prime)
