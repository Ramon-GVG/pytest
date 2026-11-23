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
    # Act: neem 30 euro op
    account.withdraw(30.0)
    # Assert: het saldo is nu 70.0
    assert account.balance == pytest.approx(70.0)


def test_withdraw_geeft_nieuw_saldo_terug(account):
    # Act: neem 25 euro op en vang het resultaat op
    result = account.withdraw(25.0)
    # Assert: withdraw() geeft het nieuwe saldo 75.0 terug
    assert result == pytest.approx(75.0)


def test_withdraw_weigert_te_hoog_bedrag(account):
    # Assert: er komt een InsufficientFundsError bij te veel opnemen
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500.0)


def test_saldo_blijft_gelijk_na_mislukte_opname(account):
    # Act: probeer 500 euro op te nemen (mislukt)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500.0)
    # Assert: het saldo is nog steeds 100.0
    assert account.balance == pytest.approx(100.0)


def test_withdraw_weigert_nul(account):
    # Assert: withdraw(0) geeft een ValueError
    with pytest.raises(ValueError):
        account.withdraw(0)


def test_hele_saldo_opnemen_mag_wel(account):
    # Act: neem precies 100.0 op (grensgeval)
    account.withdraw(100.0)
    # Assert: het saldo is nu 0.0
    assert account.balance == pytest.approx(0.0)


def test_nieuwe_rekening_met_negatief_saldo_mag_niet():
    # Assert: een BankAccount met negatief saldo geeft een ValueError
    with pytest.raises(ValueError):
        BankAccount("Test", -50)


def test_transfer_verlaagt_afzender(account, empty_account):
    # Act: maak 40 euro over van account naar empty_account
    account.transfer_to(empty_account, 40.0)
    # Assert: de afzender heeft nu 60.0
    assert account.balance == pytest.approx(60.0)


def test_transfer_verhoogt_ontvanger(account, empty_account):
    # Act: maak 40 euro over van account naar empty_account
    account.transfer_to(empty_account, 40.0)
    # Assert: de ontvanger heeft nu 40.0
    assert empty_account.balance == pytest.approx(40.0)

def test_transfer_naar_iets_dat_geen_rekening_is(account):
    # Assert: overmaken naar een string geeft een TypeError
    with pytest.raises(TypeError):
        account.transfer_to(10.0, "spaarpot")


def test_mislukte_transfer_laat_beide_rekeningen_ongemoeid(account, empty_account):
    # Act: probeer 999 euro over te maken (mislukt)
    with pytest.raises(InsufficientFundsError):
        account.transfer_to(empty_account, 999.0)
    # Assert: beide rekeningen zijn ongemoeid
    assert account.balance == pytest.approx(100.0)
    assert empty_account.balance == pytest.approx(0.0)