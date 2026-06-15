from datetime import datetime

class Calculate:
    def __init__(
            self,
            cig_in_pack: int, 
            cig_per_day: int, 
            cig_price: float
    ) -> None:
        self.cig_in_pack = cig_in_pack
        self.cig_per_day = cig_per_day
        self.cig_price = cig_price

    async def days_without_smoke(self, start_date: str) -> str:
        self.start_date = start_date
        start_date_obj = datetime.strptime(start_date, '%d.%m.%Y').date()
        today = datetime.now().date()
        days_without = (today - start_date_obj).days()