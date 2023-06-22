
input_list = input().split(", ")

check = 0

while input_list:
    check += 10
    moderated_list = [number for number in input_list if int(number) <= check]
    for rolls in range(len(input_list)):
        for element in moderated_list:
            if element in input_list:
                input_list.remove(element)
    moderated_for_print = list(map(int, moderated_list))
    print(f"Group of {check}'s: {moderated_for_print}")
    moderated_list.clear()
