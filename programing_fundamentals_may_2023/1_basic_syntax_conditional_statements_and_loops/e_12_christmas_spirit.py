quantity_of_decorations_per_each_purchase = int(input())
days_left_until_christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
total_cost = 0
spirit_gained = 0

for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations_per_each_purchase += 2
    if day % 2 == 0:
        total_cost += ornament_set * quantity_of_decorations_per_each_purchase
        spirit_gained += 5
    if day % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity_of_decorations_per_each_purchase
        spirit_gained += 13
    if day % 5 == 0:
        total_cost += tree_lights * quantity_of_decorations_per_each_purchase
        spirit_gained += 17
        if day % 3 == 0:
            spirit_gained += 30
    if day % 10 == 0:
        if day == days_left_until_christmas:
            spirit_gained -= 30
        spirit_gained -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_gained}")
