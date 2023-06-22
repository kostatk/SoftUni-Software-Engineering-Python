num_hriz = int(input())
num_rozi = int(input())
num_lale = int(input())
season = input()
holiday = input()

hriz_price = 0
rozi_price = 0
lale_price = 0
total_price = 0

if season == "Spring" or season == "Summer":
    hriz_price = 2
    rozi_price = 4.10
    lale_price = 2.50
elif season == "Autumn" or season == "Winter":
    hriz_price = 3.75
    rozi_price = 4.50
    lale_price = 4.15

total_price = hriz_price * num_hriz + rozi_price * num_rozi + lale_price * num_lale

if holiday == "Y":
    total_price *= 1.15

if num_lale > 7 and season == "Spring":
    total_price *= 0.95

if num_rozi >= 10 and season == "Winter":
    total_price *= 0.90

if num_lale + num_rozi + num_hriz > 20:
    total_price *= 0.80

final_price = total_price + 2

print(f"{final_price:.2f}")

