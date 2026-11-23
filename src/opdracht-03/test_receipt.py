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
    result = add_vat(100.0, 0.09)
    assert result == pytest.approx(109.0)


def test_apply_discount_haalt_korting_eraf():
    result = apply_discount(50.0, 10)          
    assert result == pytest.approx(45.0)


def test_apply_discount_met_nul_procent():
    result = apply_discount(50.0, 0.0)
    assert result == pytest.approx(50.0)


def test_line_total_rekent_aantal_mee():
    item = {"price": 2.50, "quantity": 4}
    result = line_total(item)
    assert result == pytest.approx(10.00)


def test_receipt_total_telt_regels_op():
    items = [
        {"price": 1.20, "quantity": 3},
        {"price": 0.95, "quantity": 2},
    ]
    result = receipt_total(items)
    assert result == pytest.approx(5.50)


def test_receipt_total_geeft_nul_bij_lege_bon():
    items = []
    result = receipt_total(items)
    assert result == pytest.approx(0.0)


def test_round_money_rondt_af_op_twee_decimalen():
    result = round_money(12.3456)
    assert result == pytest.approx(12.35)


def test_bon_met_korting_en_btw():
    amount = 200.0
    after_discount = apply_discount(amount, 25)  
    result = add_vat(after_discount, 0.21)       
    assert result == pytest.approx(181.50)