x_house_wight = float(input())
y_house_length = float(input())
h_roof_height = float(input())

front_sides_area = x_house_wight * x_house_wight * 2 - 2 * 1.2
side_sides_area = x_house_wight * y_house_length * 2 - 2 * 1.5 * 1.5

green_paint_needed = (front_sides_area + side_sides_area) / 3.4

roof_sides_area = x_house_wight * y_house_length * 2
roof_fronts_area = x_house_wight * h_roof_height # операцията / 2 * 2 я махаме

red_paint_needed = (roof_fronts_area + roof_sides_area) / 4.3

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")




