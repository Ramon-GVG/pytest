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
    result = normalize_name("ANNA SMIT")
    assert result == "Anna Smit"


def test_split_words_geeft_lege_lijst_bij_lege_tekst():
    result = split_words("")
    assert result == []


def test_count_words_telt_woorden():
    result = count_words("een twee drie")
    assert result == 3


def test_unique_words_haalt_dubbele_woorden_weg():
    result = unique_words("kat hond kat")
    assert result == ["hond", "kat"]


def test_unique_words_negeert_hoofdletters():
    result = unique_words("Kat kat KAT")
    assert result == ["kat"]


def test_word_frequency_telt_per_woord():
    result = word_frequency("kat hond kat")
    assert result == {"kat": 2, "hond": 1}


def test_word_frequency_bevat_verwacht_woord():
    result = word_frequency("appel peer appel")
    assert "appel" in result