bodybuilders = int(input())

back_trainings = 0
chest_trainings = 0
legs_trainings = 0
abss_trainings = 0
protein_shakes = 0
protein_bars = 0

for each in range(bodybuilders):
    workout = input()
    if workout == "Back":
        back_trainings += 1
    elif workout == "Chest":
        chest_trainings += 1
    elif workout == "Legs":
        legs_trainings += 1
    elif workout == "Abs":
        abss_trainings += 1
    elif workout == "Protein shake":
        protein_shakes += 1
    elif workout == "Protein bar":
        protein_bars += 1

trainers = (back_trainings + chest_trainings + legs_trainings + abss_trainings) / bodybuilders * 100
eaters = (protein_bars + protein_shakes) / bodybuilders * 100

print(f"{back_trainings} - back")
print(f"{chest_trainings} - chest")
print(f"{legs_trainings} - legs")
print(f"{abss_trainings} - abs")
print(f"{protein_shakes} - protein shake")
print(f"{protein_bars} - protein bar")
print(f"{trainers:.2f}% - work out")
print(f"{eaters:.2f}% - protein")
