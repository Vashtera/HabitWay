from aiogram import F, Router
from aiogram.types import Message

from database.requests import get_user_by_tg_id, reset_all_progress

from datetime import datetime

router = Router()


@router.message(F.text == "Я сорвался")
async def reset_all(message: Message, conn: None):
    user = await get_user_by_tg_id(message.from_user.id, conn)
    today = datetime.now().date()
    price_change_date = user["price_change_date"]
    await reset_all_progress(today, price_change_date, message.from_user.id, conn)
    await message.answer(
        "Прогресс сброшен, не отчаивайтесь и продолжайте бороться с этой привычкой"
    )
