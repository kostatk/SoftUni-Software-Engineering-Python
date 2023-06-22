
input_list = list(map(int, input().split(", ")))

positive_list = list(map(str, [number for number in input_list if number >= 0]))
negative_list = list(map(str, [number for number in input_list if number < 0]))
even_list = list(map(str, [number for number in input_list if number % 2 == 0]))
odd_list = list(map(str, [number for number in input_list if number % 2 != 0]))

print("Positive: " + ", ".join(positive_list))
print("Negative: " + ", ".join(negative_list))
print("Even: " + ", ".join(even_list))
print("Odd: " + ", ".join(odd_list))