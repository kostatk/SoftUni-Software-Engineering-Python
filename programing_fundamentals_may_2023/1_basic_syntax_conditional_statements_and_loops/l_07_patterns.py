largest_count_of_stars_on_a_row = int(input())

for row in range(1, largest_count_of_stars_on_a_row + 1):
    for stars in range(1, row + 1):
        print(f"*", end="")
    print()

for row in range(largest_count_of_stars_on_a_row - 1, 0, -1):
    for stars in range(1, row + 1):
        print(f"*", end="")
    print()
