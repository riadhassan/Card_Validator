import pytest

from validator.card_identifier import get_issuer


def test_masterCard():
    assert get_issuer("5324 3332 2152 3211") == "MasterCard"
    assert not get_issuer("4324 3332 2152 3211") == "MasterCard"


def test_visa():
    assert not get_issuer("5324 3332 2152 3211") == "Visa"
    assert get_issuer("4324 3332 2152 3211") == "Visa"
    assert get_issuer("4324 3332 2152 3") == "Visa"

def test_americanExpress():
    assert get_issuer("3424 3332 2152 3211") == "American Express"
    assert get_issuer("3724 3332 2152 3211") == "American Express"
    assert not get_issuer("4324 3332 2152 3211") == "American Express"
    assert not get_issuer("5324 3332 2152 3211") == "American Express"
    assert not get_issuer("4324 3332 2152 3") == "American Express"

def test_cardLength():
    assert get_issuer("4324 3332 2152 3256") == "Visa"
    assert get_issuer("4324 3332 2152 7") == "Visa"
    assert get_issuer("3424 3332 2152 3281") == "American Express"
    assert get_issuer("5304 3332 2152 3211") == "MasterCard"

    with pytest.raises(ValueError):
        get_issuer("4324 3332 2152")
        get_issuer("4324 3332 2152 21")
        get_issuer("4324 3332 2152 211281 25465")
