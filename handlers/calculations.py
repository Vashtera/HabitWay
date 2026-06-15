from datetime import datetime

class Calculate:
    def __init__(
            self,
            cig_in_pack: int, 
            cig_price: float
    ) -> None:
        self.cig_in_pack = cig_in_pack
        self.cig_price = cig_price

    def days_without_smoke(self, start_date: str) -> int:
        self.start_date = start_date
        start_date_obj = datetime.strptime(start_date, '%d.%m.%Y').date()
        today = datetime.now().date()
        self.days_without_smoking = (today - start_date_obj).days
        return self.days_without_smoking
    
    def total_not_smoked_cigarettes(self, cig_per_day: int) -> int:
        self.cig_per_day = cig_per_day
        total = self.days_without_smoking * cig_per_day
        return total

    