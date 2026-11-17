"""
Opdracht 7 (BONUS): Metingen Inlezen

Deze functies zijn al af. Jij schrijft de tests in test_readings_file.py

Een metingenbestand ziet er zo uit:

    sensor,value
    A1,20.0
    B2,18.5
"""


def parse_line(line):
    """Zet een regel 'A1,20.0' om naar {"sensor": "A1", "value": 20.0}."""
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"Regel moet 2 velden hebben: {line}")
    return {"sensor": parts[0].strip(), "value": float(parts[1].strip())}


def read_measurements(path):
    """Leest een metingenbestand in en geeft een lijst met dicts terug.

    De eerste regel is de kopregel en slaan we over.
    Lege regels slaan we ook over.
    """
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    measurements = []
    for line in lines[1:]:
        if line.strip() == "":
            continue
        measurements.append(parse_line(line))
    return measurements


def write_report(path, measurements):
    """Schrijft een rapportje weg met een regel per sensor.

    Elke regel ziet er zo uit:  A1: 2 metingen, gemiddeld 21.5
    De sensoren staan alfabetisch.
    """
    sensors = sorted({m["sensor"] for m in measurements})
    with open(path, "w", encoding="utf-8") as file:
        for sensor in sensors:
            values = [m["value"] for m in measurements if m["sensor"] == sensor]
            average = round(sum(values) / len(values), 1)
            file.write(f"{sensor}: {len(values)} metingen, gemiddeld {average}\n")
