budget = float (input())
season = input()

destination = "Nowhere"
place_for_rest = "Nowhere"
# За да оптимизираме кода, понеже place_for_rest има само две стойности можем в началото да я декларираме като една
# от двете стойности и само когато трябва да е другата да я презаписваме. Така всички редове където в условната
# конструкция презаписваме с първоначално избраната стойност ще отпаднат от кода. Например ако в случая я декларираме
# като "Hotel", всички редове по-долу с хотел могат да отпаднат.
money_spent = 0

if budget <= 100 and season == "summer": # ТОВА Е ВАРИАНТ 1
    destination = "Bulgaria"
    money_spent = budget * 0.3
    place_for_rest = "Camp"
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    money_spent = budget * 0.7
    place_for_rest = "Hotel"
elif budget <= 1000:                    # ТОВА Е ВАРИАНТ 2
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
        place_for_rest = "Camp"
    elif season == "winter":
        money_spent = budget * 0.8
        place_for_rest = "Hotel"
# Вариант 2 е по-добър, тъй като при него проверката за бюджета ще я прави само веднъж програмата, докато при
# Вариант 1 ще я прави всеки път и това ще забави процеса.

elif budget > 1000:
    destination = "Europe"
    money_spent = budget * 0.9
    place_for_rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_for_rest} - {money_spent:.2f}")