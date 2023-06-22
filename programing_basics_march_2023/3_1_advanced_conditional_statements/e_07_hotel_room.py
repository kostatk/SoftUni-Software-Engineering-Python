month = input()
days = int(input())

studio_price = 0
app_price = 0
studio_dis = 0
app_dis = 0

if month == "May" or month == "October":
    studio_price = 50
    app_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    app_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    app_price = 77

if days > 14:
    app_dis += 0.1
    if month == "June" or month == "September":
        studio_dis += 0.2
    elif month == "May" or month == "October":
        studio_dis += 0.3
elif days > 7 and (month == "May" or month == "October"):
    studio_dis += 0.05

total_stu = days * (studio_price * (1 - studio_dis))
total_app = days * (app_price * (1 - app_dis))

print(f"Apartment: {total_app:.2f} lv.")
print(f"Studio: {total_stu:.2f} lv.")

