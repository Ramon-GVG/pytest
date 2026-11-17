# Opdracht 5: Bankrekening

## Doel
Leer testen of je code **netjes fout gaat**, met `pytest.raises()`.

## Wat ga je doen?
Je gaat tests schrijven voor een `BankAccount` class. Deze class weigert domme dingen: geen negatieve bedragen storten, niet meer opnemen dan er op staat. In plaats van `False` terug te geven, **gooit** hij een error.

## Bestanden
- `bank_account.py` - De class die je moet testen (al klaar)
- `test_bank_account.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `deposit()` - Storten (weigert bedragen van 0 of lager)
2. `withdraw()` - Opnemen (weigert te hoge bedragen)
3. `transfer_to()` - Overmaken naar een andere rekening
4. De constructor - Weigert een negatief beginsaldo

## Wat is nieuw?
In opdracht 4 gaf `remove()` gewoon `False` terug als het niet lukte. Dat werkt, maar wie de functie aanroept kan vergeten dat te controleren. In Python is het gebruikelijker om een **error te gooien** (`raise`). Die kun je niet per ongeluk negeren: het programma stopt, tenzij iemand de error bewust afvangt.

```python
def withdraw(self, amount):
    if amount > self.balance:
        raise InsufficientFundsError("Saldo te laag")
```

En zo test je dat:

```python
with pytest.raises(InsufficientFundsError):
    account.withdraw(500)
```

Deze test slaagt als de error **wel** komt, en faalt als hij **niet** komt. Andersom dan je gewend bent!

Je kunt ook de tekst van de error checken:

```python
with pytest.raises(ValueError, match="groter dan 0"):
    account.deposit(-10)
```

`match` is een zoekopdracht in de foutmelding - je hoeft niet de hele tekst op te schrijven.

**Belangrijke valkuil:** zet alleen de regel die fout moet gaan in het `with`-blok. Je assert komt erna:

```python
with pytest.raises(InsufficientFundsError):
    account.withdraw(500)

assert account.balance == 100.0   # hier, dus niet erin
```

## Welke errors gebruikt Python?
| Error | Wanneer |
|---|---|
| `ValueError` | Waarde klopt niet (negatief bedrag) |
| `TypeError` | Verkeerd soort ding (tekst i.p.v. rekening) |
| `KeyError` | Sleutel bestaat niet in een dict |
| `ZeroDivisionError` | Delen door nul |
| Eigen error | Zoals `InsufficientFundsError` hier |

## Documentatie
- [pytest.raises](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-05/test_bank_account.py`
2. Bekijk de drie VOORBEELD tests
3. Vul de TODO's in
4. Run: `pytest src/opdracht-05`
5. Alle tests groen? Je bent klaar!

## Tips
- Denk na over welke error hoort bij welke fout - `ValueError` of `InsufficientFundsError`?
- Test niet alleen dat de error komt, maar ook dat het saldo daarna **niet** veranderd is
- `test_hele_saldo_opnemen_mag_wel` is een grensgeval: precies genoeg saldo moet wel lukken
- Een test zonder fixture-parameter kan gewoon zelf een rekening aanmaken
