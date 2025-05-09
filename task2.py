import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
print(is_valid_email("user@domain.com"))  # Output: True
print(is_valid_email("user@domain"))      # Output: False
