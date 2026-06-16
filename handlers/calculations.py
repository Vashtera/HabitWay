from datetime import datetime

from database.requests import add_money

class Calculate:
    def __init__(self):
        self.days_without_smoking = 0
        self.total_cig = 0
        self.price = 0.0
       
    def days_without_smoke(self, start_date: str) -> int:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        self.days_without_smoking = (today - start_date_obj).days
        return self.days_without_smoking
    
    def total_not_smoked_cigarettes(self, cig_per_day: int) -> int:
        self.total_cig = self.days_without_smoking * cig_per_day
        return self.total_cig

    def one_cig_price(self, cig_in_pack: int, cig_price: float) -> float:
        self.price = cig_price / cig_in_pack
        return self.price
    
    async def total_saved_money(self, conn) -> float:
        total = self.total_cig * self.price
        request = await add_money(total, conn)
        return request
