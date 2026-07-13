import random
import string


def generate_password(
    length,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    use_symbols=True
):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}<>?/"

    if not characters:
        raise ValueError("Select at least one character type.")

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password