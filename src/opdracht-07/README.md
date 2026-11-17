# Opdracht 7: Metingen Inlezen (BONUS)

## Doel
Leer code testen die **bestanden** leest en schrijft, met de fixture `tmp_path`.

## Wat ga je doen?
Je gaat tests schrijven voor code die een metingenbestand inleest en er een rapportje van maakt. De code is al af - jij schrijft de tests, net als bij de vorige opdrachten.

Dit is een bonusopdracht: maak eerst opdracht 1 t/m 6 af.

## Bestanden
- `readings_file.py` - De functies die je moet testen (al klaar)
- `test_readings_file.py` - Het test bestand waar jij tests invult

## Hoe ziet het bestand eruit?
```
sensor,value
A1,20.0
B2,18.0
A1,23.0
```

## Wat moet je testen?
1. `parse_line()` - Zet `"A1,20.0"` om naar `{"sensor": "A1", "value": 20.0}`, met een `ValueError` bij een kapotte regel
2. `read_measurements()` - Leest het hele bestand, slaat de kopregel en lege regels over
3. `write_report()` - Schrijft per sensor een regel: `A1: 2 metingen, gemiddeld 21.5`

## Wat is nieuw?
**Probleem:** hoe test je code die bestanden leest zonder je project vol te gooien met testbestanden?

**Oplossing:** `tmp_path`. Dat is een fixture die pytest zelf meelevert. Je hoeft hem niet te schrijven - zet de naam gewoon tussen de haakjes van je test, en je krijgt een lege tijdelijke map die na de test weer verdwijnt.

```python
def test_leest_bestand(tmp_path):
    path = tmp_path / "metingen.csv"            # pad in de tijdelijke map
    path.write_text("sensor,value\nA1,20.0\n")  # bestand maken
    result = read_measurements(path)
    assert len(result) == 1
```

Elke test krijgt zijn **eigen** tijdelijke map. Tests kunnen elkaars bestanden dus niet kapotmaken, en er blijft niks achter op je schijf.

`tmp_path` is een `Path` object. Handige dingen die je ermee kunt:

```python
path = tmp_path / "data.csv"     # pad samenstellen met /
path.write_text("inhoud")        # schrijven
inhoud = path.read_text()        # lezen
path.exists()                    # bestaat het?
```

Je kunt `tmp_path` ook in je **eigen** fixture gebruiken. Kijk maar naar de fixture `measurement_file` bovenaan het testbestand: die maakt een compleet metingenbestand klaar voor je.

## Code lezen: `with open(...)`
In `readings_file.py` wordt een bestand zo geopend:

```python
with open(path, encoding="utf-8") as file:
    lines = file.readlines()
```

- `open(path)` opent het bestand. Zonder extra optie is dat om te **lezen**; met `open(path, "w")` open je het om te **schrijven** (een bestaand bestand wordt dan overschreven).
- `encoding="utf-8"` zorgt dat tekens als é en ë goed gaan, op Windows en op Mac.
- `as file` geeft het geopende bestand de naam `file`, zodat je er binnen het blok mee kunt werken.
- `with` zorgt dat het bestand **automatisch weer dicht** gaat zodra het ingesprongen blok klaar is, ook als er onderweg een error komt. Zonder `with` moet je zelf `file.close()` aanroepen, en dat vergeet je makkelijk.

Bestaat het bestand niet, dan gooit `open()` zelf een `FileNotFoundError`.

## Wat heb je nodig?
- Alles van opdracht 1 t/m 6: `assert`, `==`, `in`, fixtures, `pytest.raises()`
- De fixture `tmp_path` als parameter van je test

## Documentatie
- [tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-07/test_readings_file.py`
2. Bekijk de drie VOORBEELD tests - die laten zien hoe `tmp_path` werkt
3. Vul de TODO's in
4. Run: `pytest src/opdracht-07`
5. Alle tests groen? Je bent klaar!

## Tips
- Gebruik de fixture `measurement_file` als je gewoon een bestand nodig hebt, en `tmp_path` als je zelf een bijzonder bestand wilt maken
- Let op de exacte tekst in het rapport: `A1: 2 metingen, gemiddeld 21.5` - ook bij 1 meting staat er "metingen"
- Het gemiddelde is afgerond op 1 decimaal
- Een bestand dat niet bestaat geeft een `FileNotFoundError` - die komt uit `open()` zelf
- Kijk in de tijdelijke map niet naar een bestaand bestand: elke test begint met een **lege** map
