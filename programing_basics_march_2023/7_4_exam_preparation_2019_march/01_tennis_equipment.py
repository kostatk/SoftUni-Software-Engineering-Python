from math import ceil, floor

rocket_price = float(input())
rockets = int(input())
shoes = int(input())

shoes_price = rocket_price / 6

total_price = (shoes_price * shoes + rockets * rocket_price) * 1.2

joker = total_price / 8
sponsors = total_price - joker

print(f"Price to be paid by Djokovic {floor(joker)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")
