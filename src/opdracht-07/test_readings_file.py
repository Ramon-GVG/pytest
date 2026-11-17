import pytest

from readings_file import parse_line, read_measurements, write_report


@pytest.fixture
def measurement_file(tmp_path):
    """Maakt een tijdelijk metingenbestand en geeft het pad terug."""
    path = tmp_path / "metingen.csv"
    path.write_text(
        "sensor,value\n"
        "A1,20.0\n"
        "B2,18.0\n"
        "A1,23.0\n",
        encoding="utf-8",
    )
    return path


# VOORBEELD - Een gewone test zonder bestanden
def test_voorbeeld_parse_line_zet_regel_om():
    result = parse_line("A1,20.0")
    assert result == {"sensor": "A1", "value": 20.0}


# VOORBEELD - Zo maak je een tijdelijk bestand met tmp_path
def test_voorbeeld_leest_bestand_met_een_meting(tmp_path):
    path = tmp_path / "metingen.csv"
    path.write_text("sensor,value\nA1,20.0\n", encoding="utf-8")

    result = read_measurements(path)

    assert len(result) == 1


# VOORBEELD - Een fixture die zelf tmp_path gebruikt
def test_voorbeeld_fixture_bestand_heeft_drie_metingen(measurement_file):
    assert len(read_measurements(measurement_file)) == 3


def test_parse_line_negeert_spaties():
    # TODO: Test of '  A1 , 20.0  ' netjes wordt omgezet
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_parse_line_maakt_float_van_de_waarde():
    # TODO: Parse 'A1,20' (dus zonder komma-getal)
    # TODO: Check of de value een float is
    # Hint: isinstance(result["value"], float)
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_parse_line_weigert_regel_zonder_komma():
    # TODO: Check dat parse_line('A1') een ValueError geeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_parse_line_weigert_regel_met_te_veel_velden():
    # TODO: Check dat parse_line('A1,20.0,extra') een ValueError geeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_read_measurements_slaat_kopregel_over(measurement_file):
    # TODO: Lees het bestand in
    # TODO: Check of de EERSTE meting {"sensor": "A1", "value": 20.0} is
    #       (en dus niet de kopregel!)
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_read_measurements_slaat_lege_regels_over(tmp_path):
    # TODO: Maak zelf een bestand met een paar lege regels ertussen
    # TODO: Check of alleen de echte metingen worden ingelezen
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_read_measurements_bij_alleen_een_kopregel(tmp_path):
    # TODO: Maak een bestand met alleen 'sensor,value'
    # TODO: Check of je een lege lijst terugkrijgt
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_read_measurements_bij_bestand_dat_niet_bestaat(tmp_path):
    # TODO: Probeer tmp_path / 'bestaat-niet.csv' in te lezen
    # TODO: Check dat er een FileNotFoundError komt
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_write_report_maakt_bestand_aan(tmp_path):
    # TODO: Schrijf een rapport naar tmp_path / 'rapport.txt'
    # TODO: Check met .exists() of het bestand er is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_write_report_schrijft_regel_per_sensor(tmp_path):
    # TODO: Schrijf een rapport van 3 metingen van 2 verschillende sensoren
    # TODO: Lees het bestand terug met .read_text()
    # TODO: Check of er 2 regels in staan
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_write_report_heeft_juiste_tekst(tmp_path):
    # TODO: Schrijf een rapport van 2 metingen van A1: 20.0 en 23.0
    # TODO: Check of 'A1: 2 metingen, gemiddeld 21.5' in de tekst staat
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_lezen_en_schrijven_samen(measurement_file, tmp_path):
    # TODO: Lees measurement_file in
    # TODO: Schrijf er een rapport van
    # TODO: Check of zowel A1 als B2 in het rapport staan
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
