import pytest

from receipt import (
    add_vat,
    apply_discount,
    line_total,
    receipt_total,
    round_money,
)


# VOORBEELD - Zo test je een kommagetal
def test_voorbeeld_add_vat_telt_21_procent_op():
    result = add_vat(100.0)
    assert result == pytest.approx(121.0)


# VOORBEELD - Kijk wat er gebeurt zonder approx
def test_voorbeeld_waarom_approx_nodig_is():
    # Dit is GEEN bug in Python, maar hoe computers kommagetallen opslaan.
    assert 0.1 + 0.2 != 0.3
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_add_vat_met_laag_tarief():
    # TODO: Test of add_vat(100.0, 0.09) ongeveer 109.0 is
    # Hint: gebruik pytest.approx()
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_apply_discount_haalt_korting_eraf():
    # TODO: Test of 10% korting op 50.0 uitkomt op 45.0
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_apply_discount_met_nul_procent():
    # TODO: Test of 0% korting het bedrag niet verandert
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_line_total_rekent_aantal_mee():
    # TODO: Maak een item: {"price": 2.50, "quantity": 4}
    # TODO: Check of line_total() uitkomt op 10.00
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_receipt_total_telt_regels_op():
    # TODO: Maak een lijst met 2 items:
    #   {"price": 1.20, "quantity": 3}  en  {"price": 0.95, "quantity": 2}
    # TODO: Check of het totaal ongeveer 5.50 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_receipt_total_geeft_nul_bij_lege_bon():
    # TODO: Test of een lege lijst 0.0 teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_round_money_rondt_af_op_twee_decimalen():
    # TODO: Test of 12.3456 wordt afgerond naar 12.35
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_bon_met_korting_en_btw():
    # TODO: Combineer alles!
    # TODO: Bon van 200.0, daarna 25% korting, daarna 21% BTW
    # TODO: Check of het resultaat ongeveer 181.50 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
