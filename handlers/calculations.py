from datetime import datetime

"""
Тут можно было бы и обойтись функцией, но я хотел попробовать класс
каждая выполняет свою функцию, а именно:
дней без сигарет, кол-во не выкуренных сигарет и сэкономленные деньги
каждая функция зависит друг от друга кроме последней 
"""


class Calculate:
    def __init__(self):
        self.days_without_smoking = 0
        self.total_cig = 0
        self.price = 0.0

    def days_without_smoke(self, start_date: str) -> int:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
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


"""
процесс изменения цены за сигареты которые мы получаем из add_changes
получение старой даты, прежней цены, сигаре в пачке, сигарет в день и уже о сэкономленных средствах
Если же строка в БД пуста, мы присваиваем ей 0
получаем даты в объектах для подсчета и получаем дни
Итого сначала мы считаем прежнюю цену за 1 сигарету, потом умножаем на количество в день
их же умножаем на количество имеющихся дней без сигарет до сегодняшнего дня
и полученный результат плюсуем к уже сэкономленным средствам
"""


def change_the_price_of_cigarettes(
    old_date, old_price: float, cig_in_pack: int, cig_per_day: int, saved_money: float
):
    if saved_money is None:
        saved_money = 0

    today_obj = datetime.now().date()
    days = (today_obj - old_date).days
    total = saved_money + (days * cig_per_day * (old_price / cig_in_pack))
    return round(total, 2)
