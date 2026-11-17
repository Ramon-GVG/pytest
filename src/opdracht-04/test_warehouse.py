import pytest

from warehouse import Warehouse


@pytest.fixture
def empty_warehouse():
    """Geeft elke test een vers, leeg magazijn."""
    return Warehouse("Testmagazijn")


@pytest.fixture
def filled_warehouse():
    """Geeft elke test een magazijn met voorraad erin."""
    # TODO: Maak een Warehouse aan
    # TODO: Leg er 5 muizen in en 2 laptops
    # Hint:
    #   warehouse = Warehouse("Testmagazijn")
    #   warehouse.add("muis", 5)
    #   warehouse.add("laptop", 2)
    #   return warehouse
    return None  # Vervang deze regel!


# VOORBEELD - Zo gebruik je een fixture: zet de naam tussen de haakjes
def test_voorbeeld_nieuw_magazijn_is_leeg(empty_warehouse):
    assert empty_warehouse.total_items() == 0
    assert empty_warehouse.product_count() == 0


def test_add_legt_product_in_magazijn(empty_warehouse):
    # TODO: Voeg 1 toetsenbord toe
    # TODO: Check of stock_of("toetsenbord") nu 1 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_add_met_aantal_telt_op(empty_warehouse):
    # TODO: Voeg 3 kabels toe
    # TODO: Check of total_items() nu 3 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_add_twee_keer_zelfde_product_telt_bij_elkaar(empty_warehouse):
    # TODO: Voeg 2 kabels toe, en daarna nog eens 3 kabels
    # TODO: Check of stock_of("kabel") nu 5 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_filled_warehouse_heeft_twee_producten(filled_warehouse):
    # TODO: Check of product_count() 2 is
    # Hint: je moet eerst de fixture filled_warehouse invullen!
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_remove_haalt_product_eruit(filled_warehouse):
    # TODO: Haal 2 muizen uit het magazijn
    # TODO: Check of stock_of("muis") nu 3 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_remove_geeft_false_bij_te_weinig_voorraad(filled_warehouse):
    # TODO: Probeer 10 laptops eruit te halen (er zijn er maar 2)
    # TODO: Check of remove() False teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_remove_laat_voorraad_ongemoeid_als_het_niet_lukt(filled_warehouse):
    # TODO: Probeer 10 laptops eruit te halen
    # TODO: Check of stock_of("laptop") nog steeds 2 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_product_verdwijnt_als_voorraad_op_is(filled_warehouse):
    # TODO: Haal alle 2 de laptops eruit
    # TODO: Check of product_count() nog maar 1 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_has_stock_geeft_false_bij_onbekend_product(empty_warehouse):
    # TODO: Check of has_stock("bestaat-niet") False is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_clear_maakt_magazijn_leeg(filled_warehouse):
    # TODO: Roep clear() aan
    # TODO: Check of total_items() 0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_elke_test_krijgt_een_vers_magazijn(empty_warehouse):
    # TODO: Check of dit magazijn leeg is, ook al hebben andere tests
    #       er van alles in gestopt. Dat is precies wat een fixture doet!
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
