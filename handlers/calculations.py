from datetime import datetime

from database.requests import set_price_change_date

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
    
    def total_saved_money(self, cig_in_pack: int, cig_price: float) -> float:
        price = cig_price / cig_in_pack
        total = self.total_cig * price
        return round(total, 1)
    

def change_the_price_of_cigarettes(
        old_date: str,
        old_price: float,
        cig_in_pack: int,
        cig_per_day: int,
        saved_money: float
    ):
        old_date_obj = datetime.strptime(old_date, '%Y-%m-%d').date()
        today_obj = datetime.now().date()
        days = (today_obj - old_date_obj).days
        saved_money + (days * cig_per_day * (old_price / cig_in_pack))
        


