"""
Uitleg-les: deze functies gebruiken we klassikaal om te laten zien
hoe je een test schrijft. Het testbestand vullen we samen in.
"""


def calculate_score(correct, total):
    """Berekent het scorepercentage van een quiz."""
    if total == 0:
        return 0
    return round((correct / total) * 100)


def get_rank(score):
    """Bepaalt de rang op basis van een score."""
    if score >= 90:
        return "goud"
    if score >= 70:
        return "zilver"
    if score >= 50:
        return "brons"
    return "geen"


def add_player(players, name):
    """Voegt een speler toe als die er nog niet in staat."""
    if name in players:
        return players
    return players + [name]
