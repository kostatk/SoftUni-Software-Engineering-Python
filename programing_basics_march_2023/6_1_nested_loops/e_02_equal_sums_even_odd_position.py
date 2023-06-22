num_one = int(input())
num_two = int(input())

sum_check_even = 0
sum_check_odd = 0


for num in range(num_one, num_two + 1):
    num_text = str(num)
    for ch in range(0, len(num_text)):
        if ch % 2 == 0:
            sum_check_even += int(num_text[ch])
        else:
            sum_check_odd += int(num_text[ch])
    if sum_check_even == sum_check_odd:
        print(num_text, end=" ")
    sum_check_even = 0
    sum_check_odd = 0

# ДА ВИДЯ ФУНКЦИЯТА ЕНУМЕРАТЕ