flour_price = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
baking_soda = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.10
baking_soda_price = sugar_price * 0.2

total_price = flour_price * flour + sugar_price * sugar + eggs_price * eggs + baking_soda_price * baking_soda

print(f"{total_price:.2f}")
