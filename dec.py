import re

def password_requirements(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if ' ' in password or '\t' in password:
        return False, "Password should not contain spaces or tabs."

    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    if not any(char.isalpha() for char in password):
        return False, "Password must contain at least one letter."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password meets the requirements."

def password_input():
    while True:
        password = input("Please enter a password: ")
        if not password:
            print("Password cannot be empty.")
        else:
            is_valid, message = password_requirements(password)
            if is_valid:
                print("Password meets the requirements.")
                return password
            else:
                print(f"Error: {message}")

def password_checker(func):
    def wrapper():
        while True:
            password = func()
            is_valid, message = password_requirements(password)
            if is_valid:
                print("Password meets the requirements.")
                return password
            else:
                print(f"Error: {message}")

    return wrapper

decorated_password_input = password_checker(password_input)
validated_password = decorated_password_input()
print("Your validated password:", validated_password)




