from text_utils import (
    normalize_name,
    split_words,
    count_words,
    unique_words,
    word_frequency,
)


# VOORBEELD - Deze test is al ingevuld
def test_voorbeeld_normalize_name_haalt_spaties_weg():
    result = normalize_name("  jan de vries  ")
    assert result == "Jan De Vries"


# VOORBEELD - Zo vergelijk je een hele lijst in een keer
def test_voorbeeld_split_words_geeft_lijst_terug():
    result = split_words("Hallo Wereld")
    assert result == ["hallo", "wereld"]


def test_normalize_name_zet_alles_met_hoofdletter():
    # TODO: Test of 'ANNA SMIT' wordt omgezet naar 'Anna Smit'
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_split_words_geeft_lege_lijst_bij_lege_tekst():
    # TODO: Test of '' een lege lijst [] teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_count_words_telt_woorden():
    # TODO: Test of 'een twee drie' 3 woorden heeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_unique_words_haalt_dubbele_woorden_weg():
    # TODO: Test of 'kat hond kat' de lijst ['hond', 'kat'] geeft
    # Let op: de lijst is alfabetisch gesorteerd!
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_unique_words_negeert_hoofdletters():
    # TODO: Test of 'Kat kat KAT' de lijst ['kat'] geeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_word_frequency_telt_per_woord():
    # TODO: Test of 'kat hond kat' de dict {'kat': 2, 'hond': 1} geeft
    # Hint: bij een dict maakt de volgorde niet uit voor ==
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_word_frequency_bevat_verwacht_woord():
    # TODO: Maak de frequency van 'appel peer appel'
    # TODO: Check met 'in' of 'appel' in de dict zit
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
