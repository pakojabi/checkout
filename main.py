import checkout
import discounts
import pricing_rules

if __name__ == '__main__':
    voucher = pricing_rules.Item('VOUCHER', 'Gift Card', 5.0)
    my_rules = {voucher}
    da_checkout = checkout.Checkout(my_rules)
    da_checkout.add_item('VOUCHER')
    total = da_checkout.get_total()
    print(f"total: {total}")
