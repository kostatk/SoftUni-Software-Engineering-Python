word = input()

total_sum = 0

for ch in range (0, len(word)):
    if word[ch] == "a":
        total_sum += 1
    elif word[ch] == "e":
        total_sum += 2
    elif word[ch] == "i":
        total_sum += 3
    elif word[ch] == "o":
        total_sum += 4
    elif word[ch] == "u":
        total_sum += 5

print(total_sum)
