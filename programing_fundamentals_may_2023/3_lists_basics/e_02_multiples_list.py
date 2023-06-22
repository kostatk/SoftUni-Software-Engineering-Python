factor = int(input())
count = int(input())

list_of_multiples_of_the_factor = []

for number in range(1, count + 1):
    current_multiple = factor * number
    list_of_multiples_of_the_factor.append(current_multiple)

print(list_of_multiples_of_the_factor)
