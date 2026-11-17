"""
Opdracht 6: Wachtwoordcheck

Deze functies zijn al af. Jij schrijft de tests in test_password.py
"""

SPECIAL_CHARACTERS = "!@#$%^&*?"
MIN_LENGTH = 8


def has_digit(password):
    """Zit er een cijfer in het wachtwoord?"""
    return any(character.isdigit() for character in password)


def has_uppercase(password):
    """Zit er een hoofdletter in het wachtwoord?"""
    return any(character.isupper() for character in password)


def has_special(password):
    """Zit er een leesteken in het wachtwoord?"""
    return any(character in SPECIAL_CHARACTERS for character in password)


def is_long_enough(password):
    """Is het wachtwoord lang genoeg (8 tekens of meer)?"""
    return len(password) >= MIN_LENGTH


def password_score(password):
    """Telt aan hoeveel van de 4 eisen het wachtwoord voldoet (0 t/m 4)."""
    checks = [
        is_long_enough(password),
        has_digit(password),
        has_uppercase(password),
        has_special(password),
    ]
    return sum(1 for check in checks if check)


def password_strength(password):
    """Bepaalt de sterkte: 'zwak', 'gemiddeld' of 'sterk'."""
    score = password_score(password)
    if score <= 1:
        return "zwak"
    if score <= 3:
        return "gemiddeld"
    return "sterk"


def find_problems(password):
    """Geeft een lijst met wat er nog mist aan het wachtwoord."""
    problems = []
    if not is_long_enough(password):
        problems.append("te kort")
    if not has_digit(password):
        problems.append("geen cijfer")
    if not has_uppercase(password):
        problems.append("geen hoofdletter")
    if not has_special(password):
        problems.append("geen leesteken")
    return problems
