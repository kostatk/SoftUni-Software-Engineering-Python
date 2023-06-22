from math import floor


def closes_point(x1, y1, x2, y2):
    final_x = 0
    final_y = 0
    first_point_area = x1 * y1
    second_point_area = x2 * y2
    # ЗАБИХ В ТОЗИ КОД С ТОВА КОГАТО НЯКОИ ОТ ЧЕТИРИТЕ КООРДИНАТА СА РАВНИ НА 0
    # if first_point_area == 0 or second_point_area == 0:
    #     if first_point_area != 0:
    #         final_x = floor(x2)
    #         final_y = floor(y2)
    #     elif second_point_area != 0:
    #         final_x = floor(x1)
    #         final_y = floor(y1)
    #     else:

    if abs(first_point_area) <= abs(second_point_area):
        final_x = floor(x1)
        final_y = floor(y1)
    else:
        final_x = floor(x2)
        final_y = floor(y2)
    return final_x, final_y


user_x1 = float(input())
user_y1 = float(input())
user_x2 = float(input())
user_y2 = float(input())

print_x, print_y = closes_point(user_x1, user_y1, user_x2, user_y2)
print(f"({print_x}, {print_y})")
