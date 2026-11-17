"""
Opdracht 1: Cijferlijst

Deze functies zijn al af. Jij schrijft de tests in test_grades.py
"""


def is_sufficient(grade):
    """Controleert of een cijfer voldoende is (5.5 of hoger)."""
    return grade >= 5.5


def calculate_average(grades):
    """Berekent het gemiddelde van een lijst cijfers."""
    if len(grades) == 0:
        return 0.0
    return sum(grades) / len(grades)


def highest_grade(grades):
    """Geeft het hoogste cijfer uit de lijst, of None bij een lege lijst."""
    if len(grades) == 0:
        return None
    return max(grades)


def count_sufficient(grades):
    """Telt hoeveel cijfers uit de lijst voldoende zijn."""
    total = 0
    for grade in grades:
        if is_sufficient(grade):
            total += 1
    return total
