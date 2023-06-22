length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent_preoccupied = float(input()) / 100

volume_in_cm3 = length_in_cm * width_in_cm * height_in_cm
volume_in_litres = volume_in_cm3 / 1000
preoccupied_volume = volume_in_litres * percent_preoccupied

remaining_volume_for_water = volume_in_litres - preoccupied_volume

print(remaining_volume_for_water)
