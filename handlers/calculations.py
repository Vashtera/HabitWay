class Calculate:
    def __init__(
            self, 
            start_date: str, 
            cig_in_pack: int, 
            cig_per_day: int, 
            cig_price: float
    ) -> None:
        self.start_date = start_date
        self.cig_in_pack = cig_in_pack
        self.cig_per_day = cig_per_day
        self.cig_price = cig_price

