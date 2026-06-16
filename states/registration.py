from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    start_date = State()
    cig_in_pack = State()
    cig_per_day = State()
    cig_price = State()

class Change(StatesGroup):
    cig_price_change = State()