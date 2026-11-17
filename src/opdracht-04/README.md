# Opdracht 4: Magazijn

## Doel
Leer een class testen en leer `@pytest.fixture` gebruiken om testdata klaar te zetten.

## Wat ga je doen?
Je gaat tests schrijven voor een `Warehouse` class. Omdat je in bijna elke test een magazijn nodig hebt, zet je die klaar met een **fixture**.

## Bestanden
- `warehouse.py` - De class die je moet testen (al klaar)
- `test_warehouse.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `add()` - Legt producten in het magazijn
2. `remove()` - Haalt producten eruit (geeft `False` als er te weinig is)
3. `has_stock()` - Is er genoeg voorraad?
4. `stock_of()` - Hoeveel is er van een product?
5. `total_items()` / `product_count()` - Tellen
6. `clear()` - Leegmaken

## Wat is nieuw?
Een **fixture** zet testdata klaar voordat je test begint. Je schrijft een functie met `@pytest.fixture` erboven, en die functie geeft testdata terug:

```python
@pytest.fixture
def empty_warehouse():
    return Warehouse("Testmagazijn")
```

Wil je hem gebruiken? Zet de naam dan **tussen de haakjes** van je test:

```python
def test_magazijn_is_leeg(empty_warehouse):
    assert empty_warehouse.total_items() == 0
```

pytest roept de fixture automatisch aan **voor elke test opnieuw**. Elke test krijgt dus een vers magazijn en tests kunnen elkaar niet in de war brengen.

Je vraagt de fixture per test aan, als parameter. Dat is duidelijk: je ziet aan de bovenste regel van de test precies welke data hij gebruikt.

## Wat heb je nodig?
- `import pytest`
- `@pytest.fixture` - Boven je fixture-functie
- De fixture-naam als parameter van je test

## Documentatie
- [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-04/test_warehouse.py`
2. **Belangrijk:** vul eerst de fixture `filled_warehouse` in
3. Bekijk de VOORBEELD test om te zien hoe je een fixture gebruikt
4. Vul de TODO's in
5. Run: `pytest src/opdracht-04`
6. Alle tests groen? Je bent klaar!

## Tips
- Vul `filled_warehouse` als eerste in - zonder die fixture falen veel tests
- Een fixture moet iets **returnen**, anders krijg je `None` in je test
- De laatste test bewijst het nut van fixtures: die is leeg, ook al hebben andere tests er producten in gestopt
