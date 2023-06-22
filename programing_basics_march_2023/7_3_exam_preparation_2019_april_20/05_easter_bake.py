from sys import maxsize
from math import ceil

kozunaci = int(input())

total_sugar_used = 0
total_flour_used = 0
biggest_sugar = -maxsize
biggest_flour = -maxsize

for products in range(kozunaci):
    curr_sugar_needed = int(input())
    curr_flour_needed = int(input())
    total_sugar_used += curr_sugar_needed
    total_flour_used += curr_flour_needed
    if curr_sugar_needed > biggest_sugar:
        biggest_sugar = curr_sugar_needed
    if curr_flour_needed > biggest_flour:
        biggest_flour = curr_flour_needed

sugar_packs = ceil(total_sugar_used / 950)
flour_packs = ceil(total_flour_used / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {biggest_flour} grams, max used sugar is {biggest_sugar} grams.")
