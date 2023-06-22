
word = ""
c_counter = 0
o_counter = 0
n_counter = 0

while True:
    text = input()
    if text == "End":
        break
    if text == "c" and c_counter == 0:
        c_counter += 1
        continue
    if text == "o" and o_counter == 0:
        o_counter += 1
        continue
    if text == "n" and n_counter == 0:
        n_counter += 1
        continue
    if c_counter != 0 and o_counter != 0 and n_counter != 0:
        c_counter = 0
        o_counter = 0
        n_counter = 0
        word = word + " " + text
        continue
    word = word + text

print(word)
