number_of_elements = int(input())

list_of_positive = []
list_of_negative = []

for number in range(number_of_elements):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive.append(current_number)
    else:
        list_of_negative.append(current_number)

print(list_of_positive)
print(list_of_negative)
print(f"Count of positives: {len(list_of_positive)}\nSum of negatives: {sum(list_of_negative)}")
