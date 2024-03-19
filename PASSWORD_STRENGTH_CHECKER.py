import re

def check_password_complexity(password):
    # Define criteria for password complexity
    min_length = 8
    max_length = 20
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special_char = re.search(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?`~|\\]', password)
    is_valid = True

    # Check length
    if len(password) < min_length or len(password) > max_length:
        is_valid = False
        print("Password length should be between {} and {} characters.".format(min_length, max_length))

    # Check for uppercase, lowercase, digit, and special character
    if not has_uppercase or not has_lowercase or not has_digit or not has_special_char:
        is_valid = False
        print("Password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

    return is_valid

# Example usage
password = input("Enter your password: ")
if check_password_complexity(password):
    print("Password is strong and meets complexity requirements.")
else:
    print("Password does not meet complexity requirements. Please try again.")
