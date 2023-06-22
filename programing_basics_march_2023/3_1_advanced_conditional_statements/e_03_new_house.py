flower_type = input()
num_flowers = int(input())
budget = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = num_flowers * 5
    if num_flowers > 80:
        total_price *= 0.9
elif flower_type == "Dahlias":
    total_price = num_flowers * 3.80
    if num_flowers > 90:
        total_price *= 0.85
elif flower_type == "Tulips":
    total_price = num_flowers * 2.80
    if num_flowers > 80:
        total_price *= 0.85
elif flower_type == "Narcissus":
    total_price = num_flowers * 3
    if num_flowers < 120:
        total_price *= 1.15
elif flower_type == "Gladiolus":
    total_price = num_flowers * 2.50
    if num_flowers < 80:
        total_price *= 1.2
# Можем да решим задачата и като въведем още една променлива discount и общата цена смятаме след вложената конструцкия
# Това ще ни даде повече опции след това - ако ни поискат да принтнем дискаунта или колко пари сме спестили или нещо
# друго подобно. Това е чисто програмистката логика. От гледна точна само на тази задача, моят вариант е по-добре,
# защото прави по-малко променливи и сметки.
diff = abs(total_price - budget)

if budget >= total_price:
    print(f"Hey, you have a great garden with {num_flowers} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
