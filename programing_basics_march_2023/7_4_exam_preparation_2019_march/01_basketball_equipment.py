fee = int(input())

shoes = fee * 0.6
clothes = shoes * 0.8
ball = clothes / 4
other = ball / 5

total = fee + shoes + clothes + ball + other

print(f"{total:.2f}")
