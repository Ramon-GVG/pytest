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
    result = parse_line("  A1 , 20.0  ")
    assert result == {"sensor": "A1", "value": 20.0}


def test_parse_line_maakt_float_van_de_waarde():
    result = parse_line("A1,20")
    assert isinstance(result["value"], float)


def test_parse_line_weigert_regel_zonder_komma():
    with pytest.raises(ValueError):
        parse_line("A1")


def test_parse_line_weigert_regel_met_te_veel_velden():
    with pytest.raises(ValueError):
        parse_line("A1,20.0,extra")


def test_read_measurements_slaat_kopregel_over(measurement_file):
    result = read_measurements(measurement_file)
    assert result[0] == {"sensor": "A1", "value": 20.0}


def test_read_measurements_slaat_lege_regels_over(tmp_path):
    path = tmp_path / "metingen.csv"
    path.write_text(
        "sensor,value\nA1,20.0\n\nB2,21.5\n\n",
        encoding="utf-8",
    )
    result = read_measurements(path)
    assert len(result) == 2
    assert result[0] == {"sensor": "A1", "value": 20.0}
    assert result[1] == {"sensor": "B2", "value": 21.5}


def test_read_measurements_bij_alleen_een_kopregel(tmp_path):
    path = tmp_path / "metingen.csv"
    path.write_text("sensor,value\n", encoding="utf-8")
    result = read_measurements(path)
    assert result == []


def test_read_measurements_bij_bestand_dat_niet_bestaat(tmp_path):
    path = tmp_path / "bestaat-niet.csv"
    with pytest.raises(FileNotFoundError):
        read_measurements(path)


def test_write_report_maakt_bestand_aan(tmp_path):
    path = tmp_path / "rapport.txt"
    measurements = [
        {"sensor": "A1", "value": 20.0},
        {"sensor": "A1", "value": 23.0},
    ]
    write_report(path, measurements)
    assert path.exists()


def test_write_report_schrijft_regel_per_sensor(tmp_path):
    path = tmp_path / "rapport.txt"
    measurements = [
        {"sensor": "A1", "value": 20.0},
        {"sensor": "B2", "value": 21.5},
        {"sensor": "A1", "value": 23.0},
    ]
    write_report(path, measurements)
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    assert len(lines) == 2


def test_write_report_heeft_juiste_tekst(tmp_path):
    path = tmp_path / "rapport.txt"
    measurements = [
        {"sensor": "A1", "value": 20.0},
        {"sensor": "A1", "value": 23.0},
    ]
    write_report(path, measurements)
    text = path.read_text(encoding="utf-8")
    assert "A1: 2 metingen, gemiddeld 21.5" in text


def test_lezen_en_schrijven_samen(measurement_file, tmp_path):
    measurements = read_measurements(measurement_file)
    path = tmp_path / "rapport.txt"
    write_report(path, measurements)
    text = path.read_text(encoding="utf-8")
    assert "A1" in text
    assert "B2" in text