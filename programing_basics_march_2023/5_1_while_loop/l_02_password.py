username_correct = input()
password_correct = input()

while True:
    password_input = input()
    if password_input == password_correct:
        print(f"Welcome {username_correct}!")
        break
