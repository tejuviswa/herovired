import re

def check_password_strength(password):
    """Checks the strength of a password based on predefined criteria.

    Args:
        password: The password string to be evaluated.

    Returns:
        True if the password meets the criteria, False otherwise.
    """

    # Combine criteria checks for efficiency
    if not all(
        re.search(r, password)
        for r in (
            r"[A-Z]",  # Uppercase
            r"[a-z]",  # Lowercase
            r"\d",  # Digit
            r"[^a-zA-Z0-9]",  # Special character
        )
    ):
        return False

    # AND with length check to ensure all criteria met
    return len(password) >= 8 and all(
        re.search(r, password)
        for r in (
            r"[A-Z]",  # Uppercase
            r"[a-z]",  # Lowercase
            r"\d",  # Digit
            r"[^a-zA-Z0-9]",  # Special character
        )
    )

# Example usage
password = input("Enter your password: ")

if check_password_strength(password):
    print("Your password is strong!")
else:
    print("Your password is weak. Please choose a stronger password.")
