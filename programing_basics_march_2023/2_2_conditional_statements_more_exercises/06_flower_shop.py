from math import ceil, floor

magnolii_num = int(input())
zumbuli_num = int(input())
rozi_num = int(input())
kaktusi_num = int(input())
gift_price = float(input())

total_income_lv = magnolii_num * 3.25 + zumbuli_num * 4 + rozi_num * 3.50 + kaktusi_num * 8
final_income_lv = total_income_lv * 0.95

diff = abs(final_income_lv - gift_price)

if final_income_lv >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")


