eggs_number = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_colour = ""
max_eggs = 0

for egg in range(eggs_number):
    curr_colour = input()
    if curr_colour == "red":
       red_eggs += 1
    elif curr_colour == "orange":
       orange_eggs += 1
    elif curr_colour == "blue":
       blue_eggs += 1
    elif curr_colour == "green":
       green_eggs += 1

if red_eggs > max_eggs:
    max_colour = "red"
    max_eggs = red_eggs
if orange_eggs > max_eggs:
    max_colour = "orange"
    max_eggs = orange_eggs
if blue_eggs > max_eggs:
    max_colour = "blue"
    max_eggs = blue_eggs
if green_eggs > max_eggs:
    max_colour = "green"
    max_eggs = green_eggs

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_colour}")
