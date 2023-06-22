# n_years = int(input())
# x_washing_price = float(input())
# p_toy_price = int(input())
#
# money = 0
# toys = 0
#
# for bday in range(1, n_years + 1):
#     if bday % 2 == 0:
#         money += (bday / 2 * 10) - 1
#     else:
#         toys += 1
#
# total_money = toys * p_toy_price + money
#
# diff = abs(total_money - x_washing_price)
#
# if total_money >= x_washing_price:
#     print(f"Yes! {diff:.2f}")
# else:
#     print(f"No! {diff:.2f}")

n_years = int(input())
x_washing_price = float(input())
p_toy_price = int(input())

money = 0
money_for_bday = 10

for bday in range(1, n_years + 1):
    if bday % 2 == 0:
        money += money_for_bday
        money -= 1
        money_for_bday += 10
    else:
        money += p_toy_price

diff = abs(money - x_washing_price)

if money >= x_washing_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")