class Product:
    def __init__(
        self,
        name: str,
        manufacturer: str,
        sales_param: float,
        holidays_param: float,
        vacation_param: float
    ):
        self.name = name
        self.manufacturer = manufacturer
        self.sales_param = sales_param
        self.holidays_param = holidays_param
        self.vacation_param = vacation_param
