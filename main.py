import datetime

import pandas as pd

import config
import products
from holiday import Holiday
from holidays import ALL_HOLIDAYS
from product import Product
from stores import ALL_STORES

columns = [
    "Date",
    "Product Category",
    "Product Name",
    "Manufacturer",
    "Sales Amount",
    "Warranty Days",
    "Store Location",
]
result_df = pd.DataFrame(columns=columns)


def update_future_holidays_days(
    product: Product, holiday: Holiday, current_date: datetime.date
) -> None:
    if holiday.special_event:
        product.holidays_rate_end_date = current_date + datetime.timedelta(
            days=holiday.demanded_days_after
        )
        product.previous_holidays_rate = product.special_events_param
    elif holiday.demanded_products_after:
        product.holidays_rate_end_date = current_date + datetime.timedelta(
            days=holiday.demanded_days_after
        )
        product.previous_holidays_rate = (
            product.holidays_param
            if product in holiday.demanded_products_after
            else product.sales_param * holiday.other_products_demanded_rate
        )

    if product.holidays_rate_end_date and product.holidays_rate_end_date < current_date:
        product.holidays_rate_end_date = None
        product.previous_holidays_rate = None


def get_updated_products_with_holidays_before(
    quantity: float, date: datetime.date, product: Product, holiday: Holiday
) -> (pd.DataFrame, float):
    window_start = date - datetime.timedelta(days=holiday.demanded_days_before)

    products_before_df = result_df[
        (result_df["Date"] >= window_start)
        & (result_df["Product Name"] == product.manufacturer + " " + product.name)
    ]
    if holiday.special_event:
        window_start += datetime.timedelta(4)
        quantity *= product.special_events_param
        products_before_df.loc[:, "Sales Amount"] = round(
            products_before_df.loc[:, "Sales Amount"] * product.special_events_param, 2
        )
    elif (
        holiday.demanded_products_before and product in holiday.demanded_products_before
    ):
        quantity *= product.holidays_param
        products_before_df.loc[:, "Sales Amount"] = round(
            products_before_df.loc[:, "Sales Amount"] * product.holidays_param, 2
        )
    else:
        quantity *= holiday.other_products_demanded_rate
        products_before_df.loc[:, "Sales Amount"] = round(
            products_before_df.loc[:, "Sales Amount"]
            * holiday.other_products_demanded_rate,
            2,
        )
    return products_before_df, quantity


def get_holiday(date: datetime.date) -> Holiday | None:
    current_holiday = None
    for holiday in ALL_HOLIDAYS:
        if holiday.date == date:
            current_holiday = holiday
            break

    return current_holiday


def generate_dataset(
    start_date: datetime.date, end_date: datetime.date
) -> pd.DataFrame:
    current_date = start_date

    while current_date <= end_date:
        for store in ALL_STORES:
            for product in products.ALL_PRODUCTS:
                sale_quantity = config.DEFAULT_SALE_QUANTITY
                holiday = get_holiday(current_date)

                if holiday:
                    updated_df, new_quantity = (
                        get_updated_products_with_holidays_before(
                            sale_quantity, current_date, product, holiday
                        )
                    )
                    update_future_holidays_days(product, holiday, current_date)

                    # result_df.update(updated_df)
                    result_df.loc[updated_df.index, updated_df.columns] = (
                        updated_df.values
                    )

                    sale_quantity = new_quantity
                else:
                    rate = product.sales_param

                    if product.previous_holidays_rate:
                        rate = product.previous_holidays_rate

                    sale_quantity *= rate

                sale_quantity = round(sale_quantity * store.store_rate, 2)

                new_row = {
                    "Date": current_date,
                    "Product Category": product.category,
                    "Product Name": product.manufacturer + " " + product.name,
                    "Manufacturer": product.manufacturer,
                    "Sales Amount": sale_quantity,
                    "Warranty Days": product.warranty_days,
                    "Store Location": f"{store.city} - {store.area}",
                }
                result_df.loc[len(result_df)] = new_row
        current_date += datetime.timedelta(days=1)

    return result_df


if __name__ == "__main__":
    result_df = generate_dataset(start_date=config.START_DATE, end_date=config.END_DATE)

    # Uncomment if you want to save to csv
    # result_df.to_csv("products.csv", index=False)
    result_df.to_excel("result.xlsx", index=False)
