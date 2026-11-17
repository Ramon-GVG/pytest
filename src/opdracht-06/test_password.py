import pytest

from password import (
    has_digit,
    has_uppercase,
    has_special,
    is_long_enough,
    password_score,
    password_strength,
    find_problems,
)


# VOORBEELD - Zo deed je het tot nu toe: 1 test per geval
def test_voorbeeld_has_digit_vindt_cijfer():
    assert has_digit("abc1") is True


def test_voorbeeld_has_digit_zonder_cijfer():
    assert has_digit("abc") is False


# VOORBEELD - Zelfde twee tests, maar nu met parametrize
@pytest.mark.parametrize(
    "password, expected",
    [
        ("abc1", True),
        ("abc", False),
        ("", False),
        ("1234", True),
        ("wachtwoord9", True),
    ],
)
def test_voorbeeld_has_digit_met_parametrize(password, expected):
    assert has_digit(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        # TODO: Vul hier minstens 4 gevallen in voor has_uppercase
        # Bijvoorbeeld: ("Abc", True), ("abc", False), ...
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_has_uppercase(password, expected):
    assert has_uppercase(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        # TODO: Vul hier minstens 4 gevallen in voor has_special
        # Leestekens die tellen: ! @ # $ % ^ & * ?
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_has_special(password, expected):
    assert has_special(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        # TODO: Vul hier minstens 4 gevallen in voor is_long_enough
        # Vergeet het grensgeval niet: precies 8 tekens!
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_is_long_enough(password, expected):
    assert is_long_enough(password) is expected


@pytest.mark.parametrize(
    "password, expected_score",
    [
        # TODO: Vul hier minstens 4 gevallen in voor password_score
        # De score is 0 t/m 4: lang genoeg, cijfer, hoofdletter, leesteken
        # Bijvoorbeeld: ("abc", 0), ("abcdefgh", 1), ...
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_password_score(password, expected_score):
    assert password_score(password) == expected_score


@pytest.mark.parametrize(
    "password, expected_strength",
    [
        # TODO: Vul hier minstens 6 gevallen in voor password_strength
        # Zorg dat 'zwak', 'gemiddeld' EN 'sterk' allemaal voorkomen
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_password_strength(password, expected_strength):
    assert password_strength(password) == expected_strength


def test_find_problems_bij_slecht_wachtwoord():
    # TODO: Roep find_problems("abc") aan
    # TODO: Check of alle 4 de problemen erin staan
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_find_problems_bij_perfect_wachtwoord():
    # TODO: Bedenk een wachtwoord dat aan alles voldoet
    # TODO: Check of find_problems() een lege lijst teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


@pytest.mark.parametrize(
    "password, problem",
    [
        # TODO: Vul gevallen in waarbij je checkt of EEN bepaald probleem
        #       in de lijst staat, bijvoorbeeld: ("abcdefgh", "geen cijfer")
        ("TODO", None),  # <- Haal deze regel weg als je eigen gevallen erin staan
    ],
)
def test_find_problems_bevat_probleem(password, problem):
    assert problem in find_problems(password)
