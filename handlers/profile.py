from aiogram import F, Router
from aiogram.types import Message

from database.requests import get_user_by_tg_id
from calculations import Calculate


router = Router()


@router.message(F.text == "Профиль")
async def show_profile(message: Message, pool):
    async with pool.acquire() as conn: #взяли соединение
        user = await get_user_by_tg_id(message.from_user.id, conn) #передача в requests.py
    user_days_without_smoke = Calculate.days_without_smoke(str(user['start_date']))
    total_not_smoked_cig = Calculate.total_not_smoked_cigarettes(int(user['cig_per_day']))
    await message.answer(
        f"Привет! {message.from_user_fullname}\n"
        f"Дата начала: {user['start_date']}\n" 
        f"Дней без курения: {user_days_without_smoke}\n"
        f"Сэкономлено денег: {user['total_save_money']}\n" 
        f"Не выкурено сигарет: {total_not_smoked_cig}"
    )


    


