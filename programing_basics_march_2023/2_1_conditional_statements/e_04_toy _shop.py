trip_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

total_income = num_puzzles * 2.6 + num_dolls * 3 + num_bears * 4.1 + num_minions * 8.2 + num_trucks * 2

if num_puzzles + num_dolls + num_bears + num_minions + num_trucks >= 50:
    total_income *= 0.75

profit = total_income * 0.9
differance = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {differance:.2f} lv left.")
else:
    print(f"Not enough money! {differance:.2f} lv needed.")