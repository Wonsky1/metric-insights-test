import datetime
from typing import Dict

import config
import products
from holiday import Holiday
from bs4 import BeautifulSoup
import requests


def calculate_black_friday_date(thanksgiving_date: datetime.date) -> datetime.date:
    days_ahead = 4 - thanksgiving_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_friday_date = thanksgiving_date + datetime.timedelta(days=days_ahead)
    return next_friday_date


def get_holidays() -> Dict[str, datetime.date]:
    response = requests.get(
        f"https://www.timeanddate.com/holidays/us/{config.YEAR}?hol=9"
    )
    soup = BeautifulSoup(response.text, "html.parser")

    found_holidays = soup.find_all("tr", {"class": "showrow"})
    result = {}
    for holiday in found_holidays:
        holiday_name = holiday.find("td").find_next_sibling("td").get_text(strip=True)

        if "substitute" in holiday_name:
            continue
        date_data = holiday.get("data-date")
        date_timestamp = int(date_data) / 1000
        date = datetime.date.fromtimestamp(date_timestamp)
        result[holiday_name] = date
    thanksgiving = result["Thanksgiving Day"]
    result["Black Friday"] = calculate_black_friday_date(thanksgiving)

    return result


holidays = get_holidays()

NEW_YEAR = Holiday(
    date=holidays["New Year's Day"],
    name="New Year's Day",
    demanded_products_before=products.ALL_PRODUCTS,
    demanded_products_after=products.ALL_PRODUCTS,
    demanded_days_before=13,
)

MEMORIAL_DAY = Holiday(
    date=holidays["Memorial Day"],
    name="Memorial Day",
    demanded_products_before=products.T_SHIRTS + products.PIZZA_OVENS,
    other_products_demanded_rate=1.05,
)

JUNETEENTH = Holiday(
    date=holidays["Juneteenth"],
    name="Juneteenth",
    demanded_products_before=products.T_SHIRTS + products.PIZZA_OVENS,
    other_products_demanded_rate=1.05,
)

INDEPENDENCE_DAY = Holiday(
    date=holidays["Independence Day"],
    name="Independence Day",
    demanded_products_before=products.T_SHIRTS + products.PIZZA_OVENS,
    other_products_demanded_rate=1.15,
)

LABOR_DAY = Holiday(
    date=holidays["Labor Day"],
    name="Labor Day",
    demanded_products_before=products.PIZZA_OVENS,
    other_products_demanded_rate=1.05,
)

THANKSGIVING_DAY = Holiday(
    date=holidays["Thanksgiving Day"],
    name="Thanksgiving Day",
    demanded_products_before=products.ALL_PRODUCTS,
)

CHRISTMAS_DAY = Holiday(
    date=holidays["Christmas Day"],
    name="Christmas Day",
    demanded_products_before=products.ALL_PRODUCTS,
    demanded_days_before=13,
    demanded_products_after=products.ALL_PRODUCTS,
)

BLACK_FRIDAY = Holiday(
    date=holidays["Black Friday"],
    name="Black Friday",
    demanded_days_after=13,
    special_event=True,
)

CUSTOM_HOLIDAYS = (
    CHRISTMAS_DAY,
    THANKSGIVING_DAY,
    LABOR_DAY,
    INDEPENDENCE_DAY,
    NEW_YEAR,
    MEMORIAL_DAY,
    JUNETEENTH,
    BLACK_FRIDAY,
)

for custom_holiday in CUSTOM_HOLIDAYS:
    if custom_holiday.name in holidays.keys():
        del holidays[custom_holiday.name]


ALL_HOLIDAYS = [*CUSTOM_HOLIDAYS]
for not_custom_holiday_name, not_custom_holiday_date in holidays.items():
    ALL_HOLIDAYS.append(
        Holiday(
            date=not_custom_holiday_date,
            name=not_custom_holiday_name,
            other_products_demanded_rate=1.05,
        )
    )
