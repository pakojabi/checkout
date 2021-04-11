import operator
from functools import reduce
from typing import AbstractSet

from pricing_rules import PricingRule


class Checkout:

    def __init__(self, pricing_rules: AbstractSet[PricingRule]):
        self.items = []
        self.pricing_rules = pricing_rules

    def add_item(self, item_code):
        if any(item.code == item_code for item in self.pricing_rules):
            self.items.append(item_code)
        else:
            raise ValueError

    def get_total(self) -> float:
        return reduce(lambda acc, rule: acc + rule.get_price(self.items), self.pricing_rules, 0.0)
