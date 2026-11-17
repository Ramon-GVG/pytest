# Opdracht 6: Wachtwoordcheck

## Doel
Leer veel testgevallen schrijven in weinig regels met `@pytest.mark.parametrize`.

## Wat ga je doen?
Je gaat een wachtwoordchecker testen. Zo'n checker heeft **heel veel** testgevallen: lang, kort, met cijfer, zonder hoofdletter, leeg... Als je daar elke keer een aparte testfunctie voor schrijft, ben je een uur bezig. Met `parametrize` doe je het in een paar regels.

## Bestanden
- `password.py` - De functies die je moet testen (al klaar)
- `test_password.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `has_digit()` / `has_uppercase()` / `has_special()` - Zit het erin?
2. `is_long_enough()` - Minstens 8 tekens
3. `password_score()` - Aan hoeveel van de 4 eisen wordt voldaan (0 t/m 4)
4. `password_strength()` - `'zwak'` (score 0-1), `'gemiddeld'` (score 2-3), `'sterk'` (score 4)
5. `find_problems()` - Lijst met wat er nog mist

## Wat is nieuw?
Zonder parametrize schrijf je dit:

```python
def test_has_digit_met_cijfer():
    assert has_digit("abc1") is True

def test_has_digit_zonder_cijfer():
    assert has_digit("abc") is False
```

Met parametrize schrijf je dit:

```python
@pytest.mark.parametrize("password, expected", [
    ("abc1", True),
    ("abc", False),
    ("", False),
    ("1234", True),
])
def test_has_digit(password, expected):
    assert has_digit(password) is expected
```

pytest maakt hier **4 aparte tests** van. Faalt er een, dan zie je precies welke rij fout ging:

```
FAILED test_password.py::test_has_digit[abc-False]
```

De namen tussen de eerste aanhalingstekens (`"password, expected"`) moeten precies overeenkomen met de parameters van je testfunctie.

Het is een van de handigste dingen van pytest: een nieuw testgeval toevoegen is gewoon een regel erbij in de lijst.

## Code lezen: `any()`
In `password.py` zie je regels zoals deze:

```python
return any(character.isdigit() for character in password)
```

Lees dit als: "is er **minstens één** teken in het wachtwoord dat een cijfer is?"

- `character.isdigit() for character in password` loopt langs elk teken en geeft steeds `True` of `False`
- `any(...)` geeft `True` zodra er één `True` tussen zit, anders `False`

Het doet hetzelfde als deze langere versie met een `for`-lus:

```python
for character in password:
    if character.isdigit():
        return True
return False
```

Bij een lege string zit er niks in om te controleren, dus geeft `any()` dan `False`.

## Wat heb je nodig?
- `import pytest`
- `@pytest.mark.parametrize("naam1, naam2", [(a, b), (c, d)])`
- Dezelfde namen als parameters van je testfunctie

## Documentatie
- [Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-06/test_password.py`
2. Bekijk de VOORBEELD tests: eerst de oude manier, dan met parametrize
3. Vul de lijsten met testgevallen in
4. Run: `pytest src/opdracht-06 -v` - je ziet nu elk geval apart!
5. Alle tests groen? Je bent klaar!

## Tips
- In elke lijst staat een regel `("TODO", None)` die expres faalt. Haal die weg zodra je eigen gevallen erin staan. Let op: een **lege** lijst geeft geen rode test maar een overgeslagen test (`SKIPPED`), dus vul hem echt!
- Denk aan de randgevallen: lege string, precies 8 tekens, alleen cijfers
- Reken de score eerst zelf uit voordat je hem opschrijft: `"Abcdefg1!"` voldoet aan alle 4 de eisen, dus score 4, dus `'sterk'`
- Run met `-v` om te zien hoe pytest elk geval een eigen naam geeft
- Laat elke sterkte (`zwak`, `gemiddeld`, `sterk`) minstens 2x voorkomen in je lijst
