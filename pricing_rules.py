from collections.abc import Callable


class PricingRule:
    def __init__(self, code: str, calculate_price: Callable[[list[str]], float]):
        self.code = code
        self.calculate_price = calculate_price

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

    def get_price(self, item_list) -> float:
        return self.calculate_price(item_list)


class Item(PricingRule):
    def __init__(self, code: str, name: str, unit_price: float):
        self.name = name
        self.unit_price = unit_price
        super().__init__(code, lambda items: items.count(self.code) * self.unit_price)
