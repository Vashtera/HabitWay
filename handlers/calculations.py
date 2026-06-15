from datetime import datetime

class Calculate:
       
    def days_without_smoke(self, start_date: str) -> int:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        global days_without_smoking
        days_without_smoking = (today - start_date_obj).days
        return days_without_smoking
    
    def total_not_smoked_cigarettes(self, cig_per_day: int) -> int:
        global total_cig
        total_cig = days_without_smoking * cig_per_day
        return total_cig

    def one_cig_price(self, cig_in_pack: int, cig_price: float) -> float:
        global price
        price = cig_price / cig_in_pack
        return price
    
    async def total_saved_money(self, conn) -> float:
        total = total_cig * price
        await conn.fetchrow(
        "INSERT INTO users (total_save_money) VALUES ($1)", total
        )
        return round(total, 2)
