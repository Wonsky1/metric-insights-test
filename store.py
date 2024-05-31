class Store:
    def __init__(
        self,
        name: str,
        address: str,
        area: str,
        city: str,
        state: str,
        store_rate: float = 1.0,
    ):
        self.name = name
        self.address = address
        self.city = city
        self.area = area
        self.state = state
        self.store_rate = store_rate
