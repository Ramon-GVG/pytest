"""
Opdracht 3: Kassabon

Deze functies zijn al af. Jij schrijft de tests in test_receipt.py
"""

VAT_HIGH = 0.21
VAT_LOW = 0.09


def add_vat(amount, rate=VAT_HIGH):
    """Telt BTW op bij een bedrag."""
    return amount * (1 + rate)


def apply_discount(amount, percentage):
    """Haalt een kortingspercentage van een bedrag af."""
    return amount * (1 - percentage / 100)


def line_total(item):
    """Berekent het totaal van een bonregel (prijs x aantal)."""
    return item["price"] * item["quantity"]


def receipt_total(items):
    """Telt alle bonregels bij elkaar op."""
    total = 0.0
    for item in items:
        total += line_total(item)
    return total


def round_money(amount):
    """Rondt een bedrag af op 2 decimalen."""
    return round(amount, 2)
