class PricingRule:
    def __init__(self, code: str, calculate_price):
        self.code = code
        self.calculate_price = calculate_price

    def __eq__(self, other):
        return self.code == other.code

    def get_price(self, item_list):
        return self.calculate_price(item_list)


