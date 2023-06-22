cena_skumriq = float(input())
cena_caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

cena_palamud = 1.6 * cena_skumriq
cena_safrid = 1.8 * cena_caca

neobhodimi_pari = palamud_kg * cena_palamud + safrid_kg * cena_safrid + midi_kg * 7.50

print(f"{neobhodimi_pari:.2f}")