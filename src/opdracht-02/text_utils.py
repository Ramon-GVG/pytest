"""
Opdracht 2: Tekst opschonen

Deze functies zijn al af. Jij schrijft de tests in test_text_utils.py
"""


def normalize_name(name):
    """Haalt spaties weg en zet elk woord met een hoofdletter."""
    return name.strip().title()


def split_words(text):
    """Splitst een tekst in losse woorden (kleine letters)."""
    if text.strip() == "":
        return []
    return text.lower().split()


def count_words(text):
    """Telt het aantal woorden in een tekst."""
    return len(split_words(text))


def unique_words(text):
    """Geeft de unieke woorden terug, alfabetisch gesorteerd."""
    return sorted(set(split_words(text)))


def word_frequency(text):
    """Telt hoe vaak elk woord voorkomt en geeft een dict terug."""
    frequency = {}
    for word in split_words(text):
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
