
fire_cells = input().split("#")
water_remaining = int(input())
put_out_cells = []
total_fire_put_out = 0
effort = 0

for cell in fire_cells:
    cell_list = cell.split(" = ")
    if water_remaining >= int(cell_list[1]):
        if cell_list[0] == "High" and int(cell_list[1]) in range(81, 126):
            put_out_cells.append(cell_list[1])
            water_remaining -= int(cell_list[1])
            total_fire_put_out += int(cell_list[1])
            effort += int(cell_list[1]) * 0.25
        elif cell_list[0] == "Medium" and int(cell_list[1]) in range(51, 81):
            put_out_cells.append(cell_list[1])
            water_remaining -= int(cell_list[1])
            total_fire_put_out += int(cell_list[1])
            effort += int(cell_list[1]) * 0.25
        elif cell_list[0] == "Low" and int(cell_list[1]) in range(1, 51):
            put_out_cells.append(cell_list[1])
            water_remaining -= int(cell_list[1])
            total_fire_put_out += int(cell_list[1])
            effort += int(cell_list[1]) * 0.25

print("Cells:")
for element in put_out_cells:
    print(f" - {element}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")

