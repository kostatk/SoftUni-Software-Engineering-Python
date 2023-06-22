movie_type = input()
rows = int(input())
columns = int(input())

total_tickets = rows * columns
income = 0

if movie_type == "Premiere":
    income = total_tickets * 12
# Не е лошо вместо = да слагаме += (да добавим стойност) тъй като в по-сложен код може да има нужда
# да се добави стойност, а не да се презапише напълно.
elif movie_type == "Normal":
    income = total_tickets * 7.50
elif movie_type == "Discount":
    income = total_tickets * 5

print(f"{income:.2f} leva.")

