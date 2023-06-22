weight = float(input())
service = input()
distance = int(input())

price = 0
additional = 1

if weight < 1:
    price = 3 * distance / 100
elif 1 <= weight < 10:
    price = 5 * distance / 100
elif 10 <= weight < 40:
    price = 10 * distance / 100
elif 40 <= weight < 90:
    price = 15 * distance / 100
elif 90 <= weight:
    price = 20 * distance / 100

if service == "standard":
    additional = 0
if service == "express":
    if weight < 1:
        additional = 0.8 * 3 * weight * distance / 100
    elif 1 <= weight < 10:
        additional = 0.4 * 5 * weight * distance / 100
    elif 10 <= weight < 40:
        additional = 0.05 * 10 * weight * distance / 100
    elif 40 <= weight < 90:
        additional = 0.02 * 15 * weight * distance / 100
    elif 90 <= weight:
        additional = 0.01 * 20 * weight * distance / 100

end_price = price + additional

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {end_price:.2f} lv.")