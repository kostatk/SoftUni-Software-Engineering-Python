
input_list = input().split()

modified_list = [word for word in input_list if len(word) % 2 == 0]

for word in modified_list:
    print(word)
