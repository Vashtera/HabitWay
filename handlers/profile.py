from aiogram import F, Router
from aiogram.types import Message

from database.requests import get_user_by_tg_id, get_data_from_all_tables
from handlers.calculations import Calculate


router = Router()


@router.message(F.text == "Профиль")
async def show_profile(message: Message, pool):
    async with pool.acquire() as conn: #взяли соединение
        user = await get_user_by_tg_id(message.from_user.id, conn) #передача в requests.py
        cigarette = await get_data_from_all_tables(message.from_user.id, conn) 
    user_start_date = user['start_date']
    user_total_not_smoked = cigarette['cigarettes_per_day']
    user_days_without_smoke = Calculate().days_without_smoke(str(user_start_date))
    total_not_smoked_cig = Calculate().total_not_smoked_cigarettes(int(user_total_not_smoked))
    await message.answer(
        f"Привет! {message.from_user.full_name}\n"
        f"Дата начала: {user['start_date']}\n" 
        f"Дней без курения: {user_days_without_smoke}\n"
        f"Сэкономлено денег: {user['total_save_money']}\n" 
        f"Не выкурено сигарет: {total_not_smoked_cig}"
    )


    


