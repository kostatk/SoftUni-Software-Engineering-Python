
def monthly_food(food, hay, cover, weight):
    is_enough = True
    used_food = 0
    used_hay = 0
    used_cover = 0
    for day in range(1, 31): # A day is 30 days per description
        used_food += 0.300
        if day % 2 == 0:
            used_hay += (food - used_food) * 0.05
        if day % 3 == 0:
            used_cover += weight / 3

        if used_food >= food or used_hay >= hay or used_cover >= cover:
            is_enough = False
            break

    if is_enough:
        return f"Everything is fine! Puppy is happy! Food: {(food - used_food):.2f}, Hay: {hay - used_hay:.2f}, " \
               f"Cover: {cover - used_cover:.2f}."
    return "Merry must go to the pet store!"


food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pig_weight = float(input())


result = monthly_food(food_quantity, hay_quantity, cover_quantity, pig_weight)

print(result)
