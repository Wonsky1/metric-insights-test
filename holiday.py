import datetime
from typing import Tuple

from product import Product


class Holiday:
    def __init__(
        self,
        date: datetime.date,  # DATE ex: 2023-01-07
        name: str,  # NAME ex: New Year`s Day
        demanded_products_before: (
            Tuple[Product] | None
        ) = None,  # WEEK BEFORE ex: 2023-01-01 - 2023-01-07
        demanded_products_after: (
            Tuple[Product] | None
        ) = None,  # WEEK AFTER ex: 2023-01-07 - 2023-01-14
        not_demanded_products_before: (
            Tuple[Product] | None
        ) = None,  # WEEK BEFORE ex: 2023-01-01 - 2023-01-07
        not_demanded_products_after: (
            Tuple[Product] | None
        ) = None,  # WEEK AFTER ex: 2023-01-07 - 2023-01-14
        states: Tuple[str] | None = None,  # STATES OF THE HOLIDAY ex: (DE, FL)
        other_products_demanded_rate: float = 1.0,  # DEMANDED RATE FOR OTHER PRODUCTS ex: 1.0
        not_demanded_rate: float = 0.9,  # NOT DEMANDED RATE ex: 0.9
        demanded_days_before: int = 6,
        demanded_days_after: int = 0,
        not_demanded_days_before: int = 0,
        not_demanded_days_after: int = 0,
        special_event: bool = False,  # ONLY FOR BLACK_FRIDAY
    ):
        self.date = date
        self.states = states
        self.name = name
        self.demanded_products_after = demanded_products_after
        self.demanded_products_before = demanded_products_before
        self.not_demanded_products_before = not_demanded_products_before
        self.not_demanded_products_after = not_demanded_products_after
        self.not_demanded_rate = not_demanded_rate
        self.demanded_days_before = demanded_days_before
        self.demanded_days_after = demanded_days_after
        self.not_demanded_days_before = not_demanded_days_before
        self.not_demanded_days_after = not_demanded_days_after
        self.other_products_demanded_rate = other_products_demanded_rate
        self.special_event = special_event

    def __repr__(self):
        return f"Holiday({self.date}, {self.name})"

    def __str__(self):
        return f"Holiday({self.date}, {self.name})"
