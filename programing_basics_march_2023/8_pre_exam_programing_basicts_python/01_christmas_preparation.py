paper = int(input())
cloth = int(input())
glue = float(input())
discount_percent = int(input())

total_price = (5.8 * paper + 7.20 * cloth + 1.20 * glue)

end_price = total_price * (1 - discount_percent / 100)

print(f"{end_price:.3f}")
