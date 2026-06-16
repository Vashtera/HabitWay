from aiogram import F, Router
from aiogram.types import Message

from database.requests import get_user_by_tg_id, get_data_from_all_tables
from handlers.calculations import Calculate


router = Router()


@router.message(F.text == "Профиль")
async def show_profile(message: Message, pool):
    async with pool.acquire() as conn: #взяли соединение
        #передача и получение в requests.py
        user = await get_user_by_tg_id(message.from_user.id, conn) 
        cigarette = await get_data_from_all_tables(message.from_user.id, conn)
    user_cig_price = cigarette['cigarette_price']
    user_cig_in_pack = cigarette['cigarettes_in_pack']
    user_days_without_smoke = Calculate().days_without_smoke(str(user['start_date']))
    total_not_smoked_cig = Calculate().total_not_smoked_cigarettes(int(cigarette['cigarettes_per_day']))
    user_total_saved_money = Calculate().total_saved_money(user_cig_price, user_cig_in_pack, conn)
    await message.answer(
        f"Привет! {message.from_user.full_name}\n"
        f"Дата начала: {user['start_date']}\n"  
        f"Дней без курения: {user_days_without_smoke}\n"
        f"Сэкономлено денег: {user_total_saved_money}\n" 
        f"Не выкурено сигарет: {total_not_smoked_cig}"
    )