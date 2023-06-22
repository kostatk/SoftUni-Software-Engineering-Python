days = int(input())
food = float(input())

dog_eaten = 0
cat_eaten = 0
biscuits = 0

for d in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    if d % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1
    dog_eaten += dog_food
    cat_eaten += cat_food

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(dog_eaten + cat_eaten) / food * 100:.2f}% of the food has been eaten.")
print(f"{dog_eaten / (dog_eaten + cat_eaten) * 100:.2f}% eaten from the dog.")
print(f"{cat_eaten / (dog_eaten + cat_eaten) * 100:.2f}% eaten from the cat.")
