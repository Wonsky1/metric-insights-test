from store import Store

NEW_YORK_MANHATTAN = Store(
    name="Some store",
    address="Some address",
    city="New York",
    state="NY",
    area="Manhattan",
    store_rate=1.1,
)

LOS_ANGELES_PASADENA = Store(
    name="Some store",
    address="Some address",
    city="Los Angeles",
    state="CA",
    area="Pasadena",
    store_rate=1.05,
)
CHICAGO_WICKER_PARK = Store(
    name="Some store",
    address="Some address",
    city="Chicago",
    state="IL",
    area="Wicker Park",
    store_rate=1.05,
)

OKLAHOMA_CITY_BRICKTOWN = Store(
    name="Some store",
    address="Some address",
    city="Oklahoma City",
    state="OK",
    area="Bricktown",
    store_rate=0.95,
)

ALL_STORES = (
    NEW_YORK_MANHATTAN,
    LOS_ANGELES_PASADENA,
    CHICAGO_WICKER_PARK,
    OKLAHOMA_CITY_BRICKTOWN,
)
