beginning_number = int(input())
end_num = int(input())
magic_num = int(input())

magic_counter = 0
combination_counter = 0
IS_MAGIC = False

for x in range(beginning_number, end_num + 1):
    for y in range(beginning_number, end_num + 1):
        combination_counter += 1
        if x + y == magic_num:
            IS_MAGIC = True
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_num})")
            break
    if IS_MAGIC:
        break

if not IS_MAGIC:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
