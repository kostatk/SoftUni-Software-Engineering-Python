input_list = input().split()

for element in input_list:
    current_element_list = [ch for ch in element]
    if current_element_list[2].isalpha():
        digit_code = 10 * int(current_element_list[0]) + int(current_element_list[1])
        current_element_list.pop(1)
        current_element_list[0] = chr(digit_code)
        current_element_list[-1], current_element_list[1] = current_element_list[1], current_element_list[-1]
        print("".join(current_element_list), end=" ")
    elif current_element_list[2].isnumeric():
        digit_code = 100 * int(current_element_list[0]) + 10 * int(current_element_list[1]) \
                     + int(current_element_list[2])
        current_element_list.pop(1)
        current_element_list.pop(1)
        current_element_list[0] = chr(digit_code)
        current_element_list[-1], current_element_list[1] = current_element_list[1], current_element_list[-1]
        print("".join(current_element_list), end=" ")

