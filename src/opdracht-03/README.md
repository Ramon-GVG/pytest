# Opdracht 3: Kassabon

## Doel
Leer testen met kommagetallen (floats) en `pytest.approx()`.

## Wat ga je doen?
Je gaat tests schrijven voor een kassabon: BTW erbij, korting eraf, regels optellen. Dat betekent rekenen met kommagetallen - en daar zit een valkuil in.

## Bestanden
- `receipt.py` - De functies die je moet testen (al klaar)
- `test_receipt.py` - Het test bestand waar jij tests invult

## Wat moet je testen?
1. `add_vat()` - Telt BTW op (21% standaard, 9% laag tarief)
2. `apply_discount()` - Haalt een kortingspercentage eraf
3. `line_total()` - Prijs x aantal voor een bonregel
4. `receipt_total()` - Telt alle bonregels op
5. `round_money()` - Rondt af op 2 decimalen

## Wat is nieuw?
Probeer dit eens in de Python shell:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

Dat is geen bug. Computers slaan kommagetallen binair op en dat kan niet altijd precies. Daarom faalt deze test:

```python
assert 0.1 + 0.2 == 0.3          # FAALT!
```

En deze slaagt:

```python
assert 0.1 + 0.2 == pytest.approx(0.3)   # Werkt!
```

**Regel:** test je een geheel getal? Gebruik `==`. Test je een kommagetal? Gebruik `pytest.approx()`.

Wil je strenger zijn, dan kan dat:

```python
assert totaal == pytest.approx(12.10, abs=0.01)   # max 1 cent verschil
```

> **Goed om te weten:** in echte software voor geld (webshops, banken) rekent men meestal **niet** met floats, juist door dit afrondingsprobleem. Daar gebruik je `Decimal` uit de standaardbibliotheek, of je rekent in hele centen (`1210` in plaats van `12.10`). Met `Decimal("0.1") + Decimal("0.2")` krijg je wel precies `Decimal("0.3")`. In deze opdracht houden we het simpel met floats.

## Wat heb je nodig?
- `import pytest` bovenaan je testbestand
- `pytest.approx()` - Voor alle kommagetallen
- Dicts als testdata: `{"price": 2.50, "quantity": 4}`

## Documentatie
- [pytest.approx](https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx)

## Hoe te starten?
> **Eerst:** activeer je virtual environment, anders kan je terminal `pytest` niet vinden. Zie je `(.venv)` voor je prompt? Dan zit je goed.
> - macOS / Linux: `source .venv/bin/activate`
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Windows (Opdrachtprompt / cmd): `.venv\Scripts\activate.bat`

1. Open `src/opdracht-03/test_receipt.py`
2. Bekijk de twee VOORBEELD tests - vooral de tweede!
3. Vul de TODO's in
4. Run: `pytest src/opdracht-03`
5. Alle tests groen? Je bent klaar!

## Tips
- Gebruik `pytest.approx()` bij **elke** test met een kommagetal
- De laatste opdracht combineert korting en BTW: reken eerst uit wat eruit hoort te komen (200 - 25% = 150, +21% = 181.50)
- Vergeet `import pytest` niet
