degrees = int(input())
part_of_the_day = input()

outfit = "Don't go outside. You are naked"
shoes = "Don't go outside. You are naked"

if part_of_the_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif part_of_the_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif part_of_the_day == "Evening" and degrees >= 10:
# Тук бях пропуснал, че при градуси под 10 реално условието, което ни е дадено в задачата не се изпълнява затова трябва
# да добавим и условие за градуси
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")