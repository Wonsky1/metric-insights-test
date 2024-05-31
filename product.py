class Product:
    def __init__(
        self,
        name: str,
        manufacturer: str,
        category: str,
        sales_param: float,
        holidays_param: float,
        special_events_param: float,
        warranty_days: int,
    ):
        self.holidays_rate_end_date = None
        self.previous_holidays_rate = None
        self.name = name
        self.manufacturer = manufacturer
        self.sales_param = sales_param
        self.holidays_param = holidays_param
        self.special_events_param = special_events_param
        self.warranty_days = warranty_days
        self.category = category

    def __repr__(self):
        return f"Product({self.manufacturer}, {self.name})"

    def __str__(self):
        return f"Product({self.manufacturer}, {self.name})"
