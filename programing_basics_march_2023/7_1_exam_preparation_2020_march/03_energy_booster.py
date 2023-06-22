fruit = input()
package = input()
ordered_packages = int(input())

total_price = 0

if package == "small":
    if fruit == "Watermelon":
        total_price = ordered_packages * 2 * 56
    elif fruit == "Mango":
        total_price = ordered_packages * 2 * 36.66
    elif fruit == "Pineapple":
        total_price = ordered_packages * 2 * 42.10
    elif fruit == "Raspberry":
        total_price = ordered_packages * 2 * 20
elif package == "big":
    if fruit == "Watermelon":
        total_price = ordered_packages * 5 * 28.70
    elif fruit == "Mango":
        total_price = ordered_packages * 5 * 19.60
    elif fruit == "Pineapple":
        total_price = ordered_packages * 5 * 24.80
    elif fruit == "Raspberry":
        total_price = ordered_packages * 5 * 15.20

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price: .2f} lv.")
