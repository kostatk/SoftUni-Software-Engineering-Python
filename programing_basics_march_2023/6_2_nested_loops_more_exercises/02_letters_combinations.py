beginning_letter = input()
ending_letter = input()
invalid_letter = input()

beginning_num = ord(beginning_letter)
ending_num = ord(ending_letter)
invalid_num = ord(invalid_letter)
combination_count = 0

for let_1 in range(beginning_num, ending_num + 1):
    if let_1 == invalid_num:
        continue
    for let_2 in range(beginning_num, ending_num + 1):
        if let_2 == invalid_num:
            continue
        for let_3 in range(beginning_num, ending_num + 1):
            if let_3 == invalid_num:
                continue
            combination_count += 1
            print(f"{chr(let_1)}{chr(let_2)}{chr(let_3)}", end=" ")
print(f"{combination_count}", end=" ")