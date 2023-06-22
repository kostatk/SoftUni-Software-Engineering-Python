# change_due = float(input())
# change_due *= 100
#
# coins_provided = 0
#
# while change_due > 0:
#     if change_due >= 200:
#         change_due -= 200
#
#     elif change_due >= 100:
#         change_due -= 100
#
#     elif change_due >= 50:
#         change_due -= 50
#
#     elif change_due >= 20:
#         change_due -= 20
#
#     elif change_due >= 10:
#         change_due -= 10
#
#     elif change_due >= 5:
#         change_due -= 5
#
#     elif change_due >= 2:
#         change_due -= 2
#
#     elif change_due >= 1:
#         change_due -= 1
#
#     coins_provided += 1
#
# print(coins_provided)



change_due = float(input())

coins_provided = 0

while change_due > 0:
    if change_due >= 2:
        change_due -= 2

    elif change_due >= 1:
        change_due -= 1

    elif change_due >= 0.5:
        change_due -= 0.5

    elif change_due >= 0.2:
        change_due -= 0.2

    elif change_due >= 0.1:
        change_due -= 0.1

    elif change_due >= 0.05:
        change_due -= 0.05

    elif change_due >= 0.02:
        change_due -= 0.02

    elif change_due >= 0.01:
        change_due -= 0.01

    change_due = round(change_due, 2)
    coins_provided += 1

print(coins_provided)
