from Checkout import Checkout
import pytest 
@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)

    return checkout

#def test_CanInstantiateCheckout():
#    co = Checkout()

#def test_addItemPrice(checkout):
#    checkout.addItemPrice("a", 1)

#def test_addItem(checkout):
#    checkout.addItem("a")

def test_CalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.CalculateTotal() == 1

def test_getCurrentTotal(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.CalculateTotal() == 3

def test_DiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

#@pytest.mark.skip
def test_applyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.CalculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")