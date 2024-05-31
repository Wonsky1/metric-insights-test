from product import Product


# LAPTOPS
HP_INSPIRE = Product("Inspire Laptop", "HP", "Electronics", 1.1, 1.4, 2.1, 365)
MSI_THIN_GAMING = Product(
    "Thin Gaming Laptop", "MSI", "Electronics", 1.1, 1.5, 2.0, 730
)
APPLE_MACBOOK_PRO = Product("Macbook Pro", "Apple", "Electronics", 1.2, 1.7, 1.7, 365)
APPLE_MACBOOK_AIR = Product("Macbook Air", "Apple", "Electronics", 1.2, 1.7, 1.7, 365)
ACER_ASPIRE = Product("ASPIRE", "Acer", "Laptop", 1.1, 1.4, 2.1, 365)

LAPTOPS = (
    HP_INSPIRE,
    MSI_THIN_GAMING,
    APPLE_MACBOOK_PRO,
    APPLE_MACBOOK_AIR,
    ACER_ASPIRE,
)

# T-SHIRTS
GEORGE = Product(
    "Crewneck Tee with Short Sleeves", "George", "Clothing", 1.4, 1.5, 1.5, 0
)
POLO = Product("Short Sleeve T-Shirt", "Polo", "Clothing", 1.3, 1.4, 1.4, 0)
TRUE_CLASSIC = Product(
    "Fitted Crew Neck T-Shirt", "True Classic", "Clothing", 1.3, 1.4, 1.4, 0
)
Wrangler = Product(
    "Workwear Short Sleeve T-Shirt", "Wrangler", "Clothing", 1.4, 1.5, 1.5, 0
)
GILDAN = Product("Short Sleeve vrew T-Shirt", "Gildan", "Clothing", 1.5, 1.6, 1.6, 0)

T_SHIRTS = (GEORGE, POLO, TRUE_CLASSIC, Wrangler, GILDAN)

# PIZZA OVENS
GEOPLUS = Product(
    "Commercial Pizza Stainless Steel Counter Top Snack Pan Oven Bake",
    "Geoplus",
    "Home & Kitchen",
    1.1,
    1.2,
    1.3,
    60,
)
BLACKSTONE = Product(
    "Pizza Oven with Rotating Cordierite Stone and Mobile Stand",
    "Blackstone",
    "Home & Kitchen",
    1.0,
    1.1,
    1.3,
    365,
)
PRESTO = Product("Rotating Pizza Oven", "Presto", "Home & Kitchen", 1.0, 1.2, 1.3, 365)
CUISINART = Product(
    "Pizza Oven with Two Cordierite Stones",
    "Cuisinart",
    "Home & Kitchen",
    1.1,
    1.1,
    1.3,
    1095,
)
PIZZELO = Product(
    "Pizza Oven Outdoor Pizza Oven Wood Fired",
    "Pizzelo",
    "Home & Kitchen",
    1.0,
    1.1,
    1.4,
    365,
)

PIZZA_OVENS = (GEOPLUS, BLACKSTONE, PIZZELO, CUISINART, PRESTO)

# CONSOLES
SONY_PLAYSTATION_5 = Product(
    "PlayStation 5 (PS5) Digital Console Slim",
    "Sony",
    "Electronics",
    1.1,
    1.6,
    1.9,
    365,
)
MICROSOFT_XBOX_SERIES_S = Product(
    "Xbox Series S", "Microsoft", "Electronics", 1.1, 1.6, 1.9, 365
)
NINTENDO_SWITCH = Product(
    "Switch with Gray Joy‑Con", "Nintendo", "Electronics", 1.2, 1.5, 1.9, 365
)
VALVE_STEAM_DECK = Product(
    "Steam Deck 512GB Handheld Console", "Valve", "Electronics", 1.0, 1.5, 2.0, 365
)
SONY_PLAYSTATION_PORTAL = Product(
    "PlayStation Portal Remote Player for PS5 Console",
    "Sony",
    "Electronics",
    1.0,
    1.3,
    1.6,
    365,
)

CONSOLES = (
    SONY_PLAYSTATION_5,
    VALVE_STEAM_DECK,
    MICROSOFT_XBOX_SERIES_S,
    NINTENDO_SWITCH,
    SONY_PLAYSTATION_PORTAL,
)

# ALL PRODUCTS
ALL_PRODUCTS = (*LAPTOPS, *T_SHIRTS, *PIZZA_OVENS, *CONSOLES)
