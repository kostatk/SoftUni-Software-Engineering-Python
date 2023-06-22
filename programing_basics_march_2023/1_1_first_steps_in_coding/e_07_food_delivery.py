chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

sum_for_main_food = (chicken_menu * 10.35) + (fish_menu * 12.40) + (veggie_menu * 8.15)
sum_for_dessert = sum_for_main_food * 0.20

total_sum = sum_for_main_food + sum_for_dessert + 2.50

print(total_sum)