# Pytest Testing - Opdrachten Template

Een verzameling hands-on opdrachten om unit testen te leren met pytest.

## Wat is pytest?

pytest is het testing framework voor Python. Het helpt je automatisch te checken of je code werkt zoals verwacht, zonder elke keer handmatig je script te runnen en naar de output te staren.

## Waarom Testen?

**"Kan ik niet gewoon zelf even runnen en kijken?"**

Ja, maar:

- Handmatig testen kost 5-10 minuten per keer
- Na elke code wijziging moet je ALLES opnieuw testen
- Je vergeet makkelijk edge cases (lege lijst, 0, negatief getal, None)
- Naarmate je project groeit wordt dit onhoudbaar

**Met pytest:**

- Schrijf tests 1x (10 minuten)
- Run alle tests in 2 seconden: `pytest`
- Tests vangen bugs voordat gebruikers ze zien
- Je krijgt vertrouwen om code te wijzigen

**Break-even:** Na 2-3 code wijzigingen heb je de tijd terugverdiend. Daarna is het pure winst!

## Van acceptatietest naar unit test

In de eerste twee weken van dit vak heb je een **acceptatietest** gedaan: acceptatiecriteria opstellen, een testplan schrijven, de test uitvoeren en een verbetervoorstel maken. Dat is testen op het niveau van de gebruiker, en dat doe je met de hand.

Een **unit test** zit een niveau lager: je test één functie of één class los van de rest, en de computer voert hem uit. Samen dekken ze elkaar af:

| | Acceptatietest | Unit test |
|---|---|---|
| Vraag | Doet het systeem wat de klant wil? | Doet deze functie wat ik beloofd heb? |
| Wie voert uit | Een mens | De computer |
| Hoe vaak | Bij een oplevering | Bij elke code wijziging |
| Hoe lang duurt het | Uren | Seconden |

Je acceptatiecriteria uit week 1 en 2 zijn trouwens niet voor niks: die vertalen zich vaak direct naar de testgevallen die je hier gaat opschrijven.

## De opdrachten

Bij alle opdrachten is de **code al af**. Jij schrijft de tests.

| # | Opdracht | Wat je leert |
|---|---|---|
| 1 | **Cijferlijst** | Je eerste test: `assert` en testnamen |
| 2 | **Tekst opschonen** | Lists en dicts vergelijken |
| 3 | **Kassabon** | Rekenen met floats en `pytest.approx()` |
| 4 | **Magazijn** | Een class testen met `@pytest.fixture` |
| 5 | **Bankrekening** | Foutafhandeling testen met `pytest.raises()` |
| 6 | **Wachtwoordcheck** | Veel testgevallen in weinig regels met `@pytest.mark.parametrize` |
| 7 | **Metingen Inlezen** (BONUS) | Bestanden testen met `tmp_path` |

Opdracht 7 is extra materiaal. Ben je met 1 t/m 6 klaar en heb je tijd over, ga daar dan mee verder.

## Installatie

### 1. Gebruik deze template

1. Klik op de groene knop **"Use this template"** bovenaan deze pagina
2. Kies **"Create a new repository"**
3. Geef je repository een naam (bijv. `mijn-pytest-opdrachten`)
4. Klik op **"Create repository"**
5. Clone je nieuwe repository naar je computer

### 2. Maak een virtual environment

```bash
# Windows
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

Activeren:

```bash
# Windows (PowerShell, standaard in VS Code)
.venv\Scripts\Activate.ps1

# Windows (Opdrachtprompt / cmd)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Je ziet nu `(.venv)` voor je prompt staan. Gelukt!

> **Let op:** dit activeren moet je **elke keer** doen als je een nieuwe terminal opent. Krijg je `command not found: pytest` (macOS/Linux) of `pytest is not recognized` (Windows)? Dan ben je het activeren vergeten.
>
> **Windows PowerShell geeft een rode foutmelding over "running scripts is disabled"?** Voer dan één keer dit uit en probeer het opnieuw:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

### 3. Installeer pytest

```bash
pip install -r requirements.txt
```

### 4. Test of het werkt

```bash
pytest
```

Je ziet tests falen - dat klopt! Die moet je namelijk zelf invullen.

## Hoe te gebruiken

Elke opdracht heeft een eigen map in `src/` met:

- Een bronbestand met functies die al werken
- Een testbestand met 1 of meer ingevulde **VOORBEELD** tests en een aantal **TODO** tests die jij afmaakt
- Een README.md met uitleg per opdracht

**Voorbeeld:**

```bash
pytest src/opdracht-01      # Test alleen opdracht 1
pytest                      # Test alle opdrachten
pytest -v                   # Laat elke test apart zien
pytest -k "average"         # Run alleen tests met 'average' in de naam
pytest -x                   # Stop bij de eerste fout
```

Een TODO-test ziet er zo uit:

```python
def test_is_sufficient_geeft_false_bij_vier():
    # TODO: Test of het cijfer 4.0 onvoldoende is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
```

Die regel met `assert False` vervang je door je eigen test. Zolang hij er staat is de test rood.

## pytest spiekbriefje

| Wat je wilt | Hoe |
|---|---|
| Iets is gelijk | `assert resultaat == 8` |
| Iets is waar/onwaar | `assert resultaat is True` |
| Zit in een lijst | `assert "appel" in boodschappen` |
| Kommagetallen | `assert totaal == pytest.approx(12.10)` |
| Er moet een error komen | `with pytest.raises(ValueError):` |
| Testdata klaarzetten | `@pytest.fixture` |
| Veel gevallen tegelijk | `@pytest.mark.parametrize` |
| Tijdelijk bestand | fixture `tmp_path` |

Officiele documentatie: [docs.pytest.org](https://docs.pytest.org/en/stable/)

## Tips

- Begin met opdracht 1 en werk stap voor stap door
- Elke opdracht heeft een README.md met uitleg
- Run tests vaak: `pytest src/opdracht-01`
- Lees error messages goed - pytest laat precies zien wat hij verwachtte en wat hij kreeg
- Elke test heeft 3 stappen: **Arrange** (klaarzetten), **Act** (uitvoeren), **Assert** (controleren)
- Alle tests groen? Dan ben je klaar!
