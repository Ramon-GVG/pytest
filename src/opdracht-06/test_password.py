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
        ("Abc", True),
        ("abc", False),
        ("ABC", True),
        ("wachtwoord", False),
        ("Wachtwoord1", True),
    ],
)
def test_has_uppercase(password, expected):
    assert has_uppercase(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abc!", True),
        ("abc", False),
        ("a@b", True),
        ("wachtwoord#1", True),
        ("12345", False),
    ],
)
def test_has_special(password, expected):
    assert has_special(password) is expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abcdefgh", True),
        ("abcdefg", False),
        ("abcdefghi", True),
        ("", False),
        ("12345678", True),
    ],
)
def test_is_long_enough(password, expected):
    assert is_long_enough(password) is expected


@pytest.mark.parametrize(
    "password, expected_score",
    [
        ("abc", 0),
        ("abcdefgh", 1),
        ("abcdefg1", 2),
        ("Abcdefg1", 3),
        ("Abcdefg1!", 4),
    ],
)
def test_password_score(password, expected_score):
    assert password_score(password) == expected_score


@pytest.mark.parametrize(
    "password, expected_strength",
    [
        ("abc", "zwak"),
        ("abcdefgh", "zwak"),
        ("abcdefg1", "gemiddeld"),
        ("Abcdefg1", "gemiddeld"),
        ("Abcdefg1!", "sterk"),
        ("Ab1!", "gemiddeld"),   
    ],
)
def test_password_strength(password, expected_strength):
    assert password_strength(password) == expected_strength


def test_find_problems_bij_slecht_wachtwoord():
    problems = find_problems("abc")
    assert "te kort" in problems
    assert "geen cijfer" in problems
    assert "geen hoofdletter" in problems
    assert "geen leesteken" in problems


def test_find_problems_bij_perfect_wachtwoord():
    problems = find_problems("Abcdefg1!")
    assert problems == []


@pytest.mark.parametrize(
    "password, problem",
    [
        ("abcdefgh", "geen cijfer"),
        ("abcdefg1", "geen hoofdletter"),
        ("Abcdefg1", "geen leesteken"),
        ("Ab1!", "te kort"),
        ("abc", "geen cijfer"),
    ],
)
def test_find_problems_bevat_probleem(password, problem):
    assert problem in find_problems(password)