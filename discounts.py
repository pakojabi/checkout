from pricing_rules import PricingRule, Item


class TwoForOneItem(PricingRule):
    def __init__(self, item: Item):
        super().__init__(f"TwoForOne{item.code}",
                         lambda item_list: (item_list.count(item.code) // 2) * -item.unit_price)


class ReducedPriceIfNOrMoreItems(PricingRule):
    def __init__(self, item: Item, min_items: int, new_price: float):
        super().__init__(f"ReducedPriceIf{min_items}OrMore{item.code}",
                         lambda item_list: 0 if (total := min_items.count(item.code)) < min_items
                         else (new_price - item.unit_price) * total)
