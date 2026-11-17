# Opdracht 1: Cijferlijst

## Doel
Leer de basis van testen met pytest met simpele functies.

## Wat ga je doen?
Je gaat tests schrijven voor functies die met cijfers rekenen. Er staat al **1 voorbeeld test** in het bestand. De andere tests moet jij afmaken.

## Bestanden
- `grades.py` - De functies die je moet testen (al klaar)
- `test_grades.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `is_sufficient()` - Checkt of een cijfer voldoende is (5.5 of hoger)
2. `calculate_average()` - Berekent het gemiddelde van een lijst
3. `highest_grade()` - Geeft het hoogste cijfer
4. `count_sufficient()` - Telt het aantal voldoendes

## Wat heb je nodig?
- Een functie die begint met `test_` - pytest vindt hem dan automatisch
- `assert` - Om te controleren of iets klopt
- `==` voor gelijkheid, `is True` / `is False` / `is None` voor die drie waarden

```python
def test_mijn_eerste_test():
    result = is_sufficient(7.0)
    assert result is True
```

## Wat is nieuw?
- **Testbestanden heten `test_iets.py`** en testfuncties beginnen met `test_`
- Je hebt geen speciale functies nodig om iets te controleren - alleen `assert`
- pytest laat bij een fout zien wat hij verwachtte en wat hij kreeg

## Documentatie
- [Je eerste test schrijven](https://docs.pytest.org/en/stable/getting-started.html)
- [Asserts gebruiken](https://docs.pytest.org/en/stable/how-to/assert.html)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-01/test_grades.py`
2. Lees de TODO comments
3. Vervang `assert False, "..."` met je eigen test
4. Run: `pytest src/opdracht-01`
5. Alle tests groen? Je bent klaar!

## Tips
- Begin met de voorbeeld test goed te begrijpen
- Elke test heeft 3 stappen: **Arrange** (klaarzetten), **Act** (uitvoeren), **Assert** (controleren)
- Let op de grensgevallen: precies 5.5, en een lege lijst
- Run `pytest src/opdracht-01 -v` om elke test apart te zien
