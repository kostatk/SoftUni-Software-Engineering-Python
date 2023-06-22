key = int(input())
number_of_inputs = int(input())
decrypted_message = ""

for letter in range(number_of_inputs):
    current_letter = input()
    current_digit = ord(current_letter) + key
    decrypted_message += chr(current_digit)

print(decrypted_message)
