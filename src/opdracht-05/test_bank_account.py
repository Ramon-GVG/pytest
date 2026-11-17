import pytest

from bank_account import BankAccount, InsufficientFundsError


@pytest.fixture
def account():
    """Een rekening met 100 euro erop."""
    return BankAccount("Sam", 100.0)


@pytest.fixture
def empty_account():
    """Een rekening zonder saldo."""
    return BankAccount("Robin")


# VOORBEELD - Een gewone test, zoals je gewend bent
def test_voorbeeld_deposit_verhoogt_saldo(account):
    account.deposit(50.0)
    assert account.balance == pytest.approx(150.0)


# VOORBEELD - Zo test je dat er een error KOMT
def test_voorbeeld_deposit_weigert_negatief_bedrag(account):
    with pytest.raises(ValueError):
        account.deposit(-10.0)


# VOORBEELD - Zo test je ook nog de tekst van de error
def test_voorbeeld_error_heeft_de_juiste_tekst(account):
    with pytest.raises(ValueError, match="groter dan 0"):
        account.deposit(0)


def test_withdraw_verlaagt_saldo(account):
    # TODO: Neem 30 euro op
    # TODO: Check of het saldo nu 70.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_withdraw_geeft_nieuw_saldo_terug(account):
    # TODO: Check of withdraw(25.0) het getal 75.0 teruggeeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_withdraw_weigert_te_hoog_bedrag(account):
    # TODO: Probeer 500 euro op te nemen van een rekening met 100 euro
    # TODO: Check dat er een InsufficientFundsError komt
    # Hint: with pytest.raises(InsufficientFundsError):
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_saldo_blijft_gelijk_na_mislukte_opname(account):
    # TODO: Probeer 500 euro op te nemen (gebruik pytest.raises)
    # TODO: Check daarna of het saldo nog steeds 100.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_withdraw_weigert_nul(account):
    # TODO: Check dat withdraw(0) een ValueError geeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_hele_saldo_opnemen_mag_wel(account):
    # TODO: Neem precies 100.0 op (grensgeval!)
    # TODO: Check of het saldo 0.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_nieuwe_rekening_met_negatief_saldo_mag_niet():
    # TODO: Check dat BankAccount("Test", -50) een ValueError geeft
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_transfer_verlaagt_afzender(account, empty_account):
    # TODO: Maak 40 euro over van account naar empty_account
    # TODO: Check of account.balance nu 60.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_transfer_verhoogt_ontvanger(account, empty_account):
    # TODO: Maak 40 euro over van account naar empty_account
    # TODO: Check of empty_account.balance nu 40.0 is
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_transfer_naar_iets_dat_geen_rekening_is(account):
    # TODO: Probeer 10 euro over te maken naar de tekst "spaarpot"
    # TODO: Check dat er een TypeError komt
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"


def test_mislukte_transfer_laat_beide_rekeningen_ongemoeid(account, empty_account):
    # TODO: Probeer 999 euro over te maken (dat lukt niet)
    # TODO: Check dat account nog 100.0 heeft en empty_account nog 0.0
    assert False, "Deze test faalt! Vervang deze regel met je eigen test"
