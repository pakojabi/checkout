from pricing_rules import PricingRule, Item


class TwoForOneItem(PricingRule):
    def __init__(self, item: Item):
        super().__init__(f"TwoForOne{item.code}",
                         lambda item_list: (item_list.count(item.code) // 2) * -item.unit_price)
