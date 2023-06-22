points = int(input())

bonus = 0

if points <= 100:
    bonus += 5
elif 1000 > points > 100:
    bonus = points * 0.2
elif points > 1000:
    bonus = points * 0.1

if points % 2 == 0:
    bonus += 1 # Това е същото като bonus = bonus + 1
elif points % 10 == 5:
    bonus += 2

new_points = points + bonus
print(bonus)
print(new_points)


# пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса).