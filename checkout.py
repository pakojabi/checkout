from functools import reduce
from typing import AbstractSet

from pricing_rules import PricingRule


class Checkout:
    items = []

    def __init__(self, pricing_rules: AbstractSet[PricingRule]):
        self.pricing_rules = pricing_rules

    def add_item(self, item_code):
        self.items.append(item_code)

    def get_total(self) -> float:
        return reduce(sum, list(map(lambda rule: rule.get_price(self.items), self.pricing_rules)))
