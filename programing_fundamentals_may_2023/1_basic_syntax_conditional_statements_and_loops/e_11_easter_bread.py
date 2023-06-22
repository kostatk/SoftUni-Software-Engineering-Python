budget = float(input())
price_for_kg_flour = float(input())
price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_liter_milk = price_for_kg_flour * 1.25
price_of_one_loaf = price_for_kg_flour + price_for_pack_eggs + price_for_liter_milk / 4
loafs_made_counter = 0
coloured_eggs_counter = 0



while budget > price_of_one_loaf:
    loafs_made_counter += 1
    budget -= price_of_one_loaf
    coloured_eggs_counter += 3
    if loafs_made_counter % 3 == 0:
        coloured_eggs_counter -= loafs_made_counter - 2

print(f"You made {loafs_made_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs "
      f"and {budget:.2f}BGN left.")