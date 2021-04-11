import unittest
from checkout import Checkout
from discounts import TwoForOneItem, ReducedPriceIfNOrMoreItems
from pricing_rules import Item


class MyTestCase(unittest.TestCase):
    def test_empty_cart_with_no_rules_is_0(self):
        my_rules = {}
        sut = Checkout(my_rules)
        self.assertEqual(0.0, sut.get_total())

    def test_emtpy_cart_with_rules_is_0(self):
        my_rules = {Item('VOUCHER', 'Gift Card', 5.0)}
        sut = Checkout(my_rules)
        self.assertEqual(0.0, sut.get_total())

    def test_rules_with_only_items_add_item_values_in_the_cart(self):
        my_rules = {Item('VOUCHER', 'Gift Card', 5.0),
                    Item('TSHIRT', 'Summer T-Shirt', 20.0),
                    Item('PANTS', 'Summer Pants', 7.5)}
        sut = Checkout(my_rules)
        sut.add_item('VOUCHER')
        sut.add_item('TSHIRT')
        sut.add_item('PANTS')
        expected_total = 32.5
        self.assertEqual(expected_total, sut.get_total())

    def test_total_remains_unaltered_when_discounts_do_not_apply(self):
        voucher_desc = Item('VOUCHER', 'Gift Card', 5.0)
        tshirt_desc = Item('TSHIRT', 'Summer T-Shirt', 20.0)
        pants_desc = Item('PANTS', 'Summer Pants', 7.5)

        my_rules = {voucher_desc, tshirt_desc, pants_desc,
                    TwoForOneItem(voucher_desc),
                    ReducedPriceIfNOrMoreItems(tshirt_desc, 3, 19.0)}

        sut = Checkout(my_rules)
        sut.add_item('VOUCHER')
        sut.add_item('TSHIRT')
        sut.add_item('PANTS')
        expected_total = 32.5

        self.assertEqual(expected_total, sut.get_total())


if __name__ == '__main__':
    unittest.main()
