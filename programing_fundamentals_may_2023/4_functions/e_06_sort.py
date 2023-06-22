
user_word = input().split()
numbers_list = []
for element in user_word:
    numbers_list.append(int(element))

print(sorted(numbers_list))
