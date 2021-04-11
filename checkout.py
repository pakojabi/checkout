class Checkout:
    items = []

    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules

    def add_item(self, item_code):
        self.items.append(item_code)

    def get_total(self) -> float:
        return 0.0


