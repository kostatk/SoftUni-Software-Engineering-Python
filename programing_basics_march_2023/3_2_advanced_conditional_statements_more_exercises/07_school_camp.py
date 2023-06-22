season = input()
group_type = input()
num_kids = int(input())
num_nights = int(input())

sport = ""
price_per_night = ""
price = 0
discount = 0

if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        price = 9.60
    elif group_type == "girls":
        sport = "Gymnastics"
        price = 9.60
    elif group_type == "mixed":
        sport = "Ski"
        price = 10
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        price = 7.20
    elif group_type == "girls":
        sport = "Athletics"
        price = 7.20
    elif group_type == "mixed":
        sport = "Cycling"
        price = 9.50
elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
        price = 15
    elif group_type == "girls":
        sport = "Volleyball"
        price = 15
    elif group_type == "mixed":
        sport = "Swimming"
        price = 20

if num_kids >= 50:
    discount = 0.5
elif 50 > num_kids >= 20:
    discount = 0.15
elif 20 > num_kids >= 10:
    discount = 0.05

total_price = price * num_kids * num_nights * (1 - discount)

print(f"{sport} {total_price:.2f} lv.")