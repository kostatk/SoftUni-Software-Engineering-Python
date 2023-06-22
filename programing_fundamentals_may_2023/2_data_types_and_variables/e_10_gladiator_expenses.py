lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses_for_helmet = 0
expenses_for_sword = 0
expenses_for_shield = 0
expenses_for_armor = 0
broken_shields = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses_for_helmet += helmet_price
    if fight % 3 == 0:
        expenses_for_sword += sword_price
    if fight % 6 == 0:
        expenses_for_shield += shield_price
        broken_shields += 1
        if broken_shields % 2 == 0:
            expenses_for_armor += armor_price

total_expenses = expenses_for_helmet + expenses_for_sword + expenses_for_shield + expenses_for_armor

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
