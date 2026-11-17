# Opdracht 2: Tekst opschonen

## Doel
Leer hoe je lists en dicts test.

## Wat ga je doen?
Je gaat tests schrijven voor functies die tekst opschonen en analyseren. Deze functies geven geen simpel getal terug, maar een **lijst** of een **dict**.

## Bestanden
- `text_utils.py` - De functies die je moet testen (al klaar)
- `test_text_utils.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `normalize_name()` - Haalt spaties weg, zet hoofdletters goed
2. `split_words()` - Splitst tekst in losse woorden
3. `count_words()` - Telt woorden
4. `unique_words()` - Unieke woorden, alfabetisch
5. `word_frequency()` - Telt hoe vaak elk woord voorkomt (dict)

## Wat is nieuw?
In Python vergelijk je een hele lijst of dict gewoon met `==`. Je hoeft niet per element te checken:

```python
assert split_words("a b") == ["a", "b"]
assert word_frequency("a a") == {"a": 2}
```

Bij een dict maakt de **volgorde niet uit** voor `==`. Bij een lijst wel!

Wil je alleen checken of iets erin zit, gebruik dan `in`:

```python
assert "appel" in resultaat
assert "peer" not in resultaat
```

## Code lezen: `set()` en `sorted()`
In `text_utils.py` staat deze regel:

```python
return sorted(set(split_words(text)))
```

Lees hem van binnen naar buiten:

1. `split_words(text)` maakt een lijst woorden: `["kat", "hond", "kat"]`
2. `set(...)` maakt daar een **set** van: een verzameling waarin alles maar één keer voorkomt. Dubbele woorden verdwijnen: `{"kat", "hond"}`. Een set heeft geen vaste volgorde.
3. `sorted(...)` maakt er weer een **lijst** van, alfabetisch gesorteerd: `["hond", "kat"]`

Daarom kun je het resultaat van `unique_words()` gewoon met `==` vergelijken met een lijst.

## Wat heb je nodig?
- `==` - Voor hele lijsten en dicts
- `in` / `not in` - Om te checken of iets erin zit
- `len()` - Om de lengte te checken

## Documentatie
- [Asserts gebruiken](https://docs.pytest.org/en/stable/how-to/assert.html)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-02/test_text_utils.py`
2. Bekijk eerst de twee VOORBEELD tests
3. Vul de TODO's in
4. Run: `pytest src/opdracht-02`
5. Alle tests groen? Je bent klaar!

## Tips
- Faalt je lijst-test? Kijk goed naar de **volgorde** en naar **hoofdletters**
- pytest laat bij lijsten precies zien welk element anders is
- `unique_words()` geeft een gesorteerde lijst terug - dus alfabetisch, niet de volgorde van de tekst
