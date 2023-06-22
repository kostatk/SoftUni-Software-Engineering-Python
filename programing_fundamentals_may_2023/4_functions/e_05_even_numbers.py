
def is_even(a):
    if a % 2 == 0:
        return True
    return False


user_word = input().split()
numbers_to_check = []
for element in user_word:
    numbers_to_check.append(int(element))

filtered = list(filter(is_even, numbers_to_check))

print(filtered)

