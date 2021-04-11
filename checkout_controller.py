from checkout import Checkout
from discounts import TwoForOneItem, ReducedPriceIfNOrMoreItems
from pricing_rules import Item


class CheckoutController:
    voucher_desc = Item('VOUCHER', 'Gift Card', 5.0)
    tshirt_desc = Item('TSHIRT', 'Summer T-Shirt', 20.0)
    pants_desc = Item('PANTS', 'Summer Pants', 7.5)

    rules = {voucher_desc, tshirt_desc, pants_desc,
             TwoForOneItem(voucher_desc),
             ReducedPriceIfNOrMoreItems(tshirt_desc, 3, 19.0)}

    def __init__(self):
        self.checkout = Checkout(self.rules)

    def clear_checkout(self):
        self.checkout = Checkout(self.rules)

    def add_item(self, item_name):
        try:
            self.checkout.add_item(item_name)
            return True
        except ValueError:
            return False

    def get_total(self):
        return self.checkout.get_total()
