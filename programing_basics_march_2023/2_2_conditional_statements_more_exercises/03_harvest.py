from math import floor, ceil

vineyard_area = int(input())
kg_grapes_per_sqm = float(input())
wine_needed_in_litres = int(input())
num_workers = int(input())

total_grapes_kg = vineyard_area * kg_grapes_per_sqm
total_wine = 0.4 * total_grapes_kg / 2.5
diff = abs(total_wine - wine_needed_in_litres)
wine_per_worker = 0

if total_wine < wine_needed_in_litres:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    wine_per_worker += diff / num_workers
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_worker)} liters per person.")




