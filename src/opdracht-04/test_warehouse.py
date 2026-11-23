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
    # Act: voeg 1 toetsenbord toe
    empty_warehouse.add("toetsenbord", 1)
    # Assert: check of de voorraad nu 1 is
    assert empty_warehouse.stock_of("toetsenbord") == 1


def test_add_met_aantal_telt_op(empty_warehouse):
    # Act: voeg 3 kabels toe
    empty_warehouse.add("kabel", 3)
    # Assert: check of total_items() nu 3 is
    assert empty_warehouse.total_items() == 3


def test_add_twee_keer_zelfde_product_telt_bij_elkaar(empty_warehouse):
    # Act: voeg 2 kabels toe, en daarna nog eens 3 kabels
    empty_warehouse.add("kabel", 2)
    empty_warehouse.add("kabel", 3)
    # Assert: check of stock_of("kabel") nu 5 is
    assert empty_warehouse.stock_of("kabel") == 5


def test_filled_warehouse_heeft_twee_producten(empty_warehouse):
    # Zelf vullen in plaats van vertrouwen op filled_warehouse
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Assert: er zijn 2 producten
    assert empty_warehouse.product_count() == 2


def test_remove_haalt_product_eruit(empty_warehouse):
    # Zelf vullen
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Act: haal 2 muizen eruit
    empty_warehouse.remove("muis", 2)
    # Assert: er zijn nog 3 muizen
    assert empty_warehouse.stock_of("muis") == 3


def test_remove_geeft_false_bij_te_weinig_voorraad(empty_warehouse):
    # Zelf vullen
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Act: probeer 10 laptops eruit te halen
    result = empty_warehouse.remove("laptop", 10)
    # Assert: remove() geeft False terug
    assert result is False


def test_remove_laat_voorraad_ongemoeid_als_het_niet_lukt(empty_warehouse):
    # Zelf vullen
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Act: probeer 10 laptops eruit te halen (mislukt)
    empty_warehouse.remove("laptop", 10)
    # Assert: de voorraad laptops is nog steeds 2
    assert empty_warehouse.stock_of("laptop") == 2


def test_product_verdwijnt_als_voorraad_op_is(empty_warehouse):
    # Zelf vullen
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Act: haal alle 2 de laptops eruit
    empty_warehouse.remove("laptop", 2)
    # Assert: er is nog maar 1 product over (alleen muizen)
    assert empty_warehouse.product_count() == 1


def test_has_stock_geeft_false_bij_onbekend_product(empty_warehouse):
    # Assert: een onbekend product heeft geen voorraad
    assert empty_warehouse.has_stock("bestaat-niet") is False


def test_clear_maakt_magazijn_leeg(empty_warehouse):
    # Zelf vullen
    empty_warehouse.add("muis", 5)
    empty_warehouse.add("laptop", 2)
    # Act: maak het magazijn leeg
    empty_warehouse.clear()
    # Assert: total_items() is nu 0
    assert empty_warehouse.total_items() == 0


def test_elke_test_krijgt_een_vers_magazijn(empty_warehouse):
    # Assert: dit magazijn is leeg, ook al hebben andere tests
    #         er van alles in gestopt. Dat is precies wat een fixture doet!
    assert empty_warehouse.total_items() == 0
    assert empty_warehouse.product_count() == 0