from sys import maxsize

num_numbers = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for i in range(1, num_numbers + 1):
    curr_number = float(input())
    if i % 2 == 0:
        even_sum += curr_number
        if curr_number < even_min:
            even_min = curr_number
        if curr_number > even_max:
            even_max = curr_number
    else:
        odd_sum += curr_number
        if curr_number < odd_min:
            odd_min = curr_number
        if curr_number > odd_max:
            odd_max = curr_number

print(f"OddSum={odd_sum:.2f},")
if odd_min != maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")
if odd_max != -maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")
if even_max != -maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")
