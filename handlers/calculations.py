from datetime import datetime

class Calculate:
       
    def days_without_smoke(self, start_date: str) -> int:
        start_date_obj = datetime.strptime(start_date, '%d.%m.%Y').date()
        today = datetime.now().date()
        self.days_without_smoking = (today - start_date_obj).days
        return self.days_without_smoking
    
    def total_not_smoked_cigarettes(self, cig_per_day: int) -> int:
        self.total_cig = self.days_without_smoking * cig_per_day
        return self.total_cig

    def one_cig_price(self, cig_in_pack: int, cig_price: float) -> float:
        self.price = cig_price / cig_in_pack
        return self.price
    
    def total_saved_money(self) -> float:
        total = self.total_cig * self.price
        return round(total, 2)
