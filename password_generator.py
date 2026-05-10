#!/usr/bin/env python3
"""Console password generator script."""

from __future__ import annotations

import secrets
import string


def generate_password(length: int) -> str:
    """Generate a password of the given length with mixed character types.

    The password will contain at least one lowercase letter, one uppercase
    letter, one digit, and one punctuation character. The remaining characters
    are selected at random from the combined character set.
    """
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")

    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    punctuation = secrets.choice("!@#$%^&*()-_=+[]{};:,.<>?/|")

    remaining_length = length - 4
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/|"
    remaining_chars = [secrets.choice(alphabet) for _ in range(remaining_length)]

    password_chars = [lowercase, uppercase, digit, punctuation, *remaining_chars]
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main() -> None:
    while True:
        try:
            user_input = input("Введите желаемую длину пароля: ").strip()
            length = int(user_input)
            password = generate_password(length)
        except ValueError as error:
            print(f"Ошибка: {error}. Попробуйте снова.")
        else:
            print(f"Сгенерированный пароль: {password}")
            break


if __name__ == "__main__":
    main()
