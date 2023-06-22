number = int(input())
NOT_SPECIAL = False

for num in range(1111, 10000):
    num_text = str(num)
    for i in range(0, len(num_text)):
        if int(num_text[i]) == 0:
            NOT_SPECIAL = True
            break
        if number % (int(num_text[i])) != 0:
            NOT_SPECIAL = True
            break
    if not NOT_SPECIAL:
        print(num, end=" ")
    NOT_SPECIAL = False
