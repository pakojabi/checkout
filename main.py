import checkout
import discounts
import pricing_rules

if __name__ == '__main__':
    voucher = pricing_rules.Item('VOUCHER', 'Gift Card', 5.0)
    tshirt = pricing_rules.Item('TSHIRT', 'Summer T-Shirt', 20.0)
    pants = pricing_rules.Item('PANTS', 'Summer Pants', 7.50)

    my_rules = {voucher, tshirt, pants}
    da_checkout = checkout.Checkout(my_rules)
    da_checkout.add_item('VOUCHER')
    da_checkout.add_item('TSHIRT')
    da_checkout.add_item('PANTS')
    total = da_checkout.get_total()
    print(f"total: {total}")
