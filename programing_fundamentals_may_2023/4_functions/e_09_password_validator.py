
def password_validation(password):
    is_valid = True
    num_counter = 0
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        # if ord(character) not in range(48, 58)\
        #     or ord(character) not in range(65, 91)\
        #     or ord(character) not in range(97, 123):
        print("Password must consist only of letters and digits")
        is_valid = False
    for character in password:
        if character.isnumeric():
            num_counter += 1
    if num_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


user_password = input()
password_validation(user_password)
