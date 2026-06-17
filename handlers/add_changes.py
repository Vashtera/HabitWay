from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.requests import change_the_price, get_data_from_all_tables,set_price_change_date
from handlers.calculations import change_the_price_of_cigarettes
from states.registration import Change


router = Router()

@router.message(F.text == "Изменить данные")
async def start_changes(message: Message, state: FSMContext):
    await state.set_state(Change.cig_price_change)
    await message.answer("Введите новую цену за пачку сигарет")

@router.message(Change.cig_price_change)
async def register_change(message: Message, state: FSMContext, conn: None):
    try:
        val_price = float(message.text)
    except ValueError:
        await message.answer("Пожалуйста введите число")
        return
    await state.update_data(cig_price_change = val_price)
    user = await get_data_from_all_tables(message.from_user.id, conn)
    today_str = today_obj.strftime('%Y-%m-%d')
    user_old_date = user.get('start_date')
    user_old_price = user.get('cigarette_price')
    user_cig_in_pack = user.get('cigarettes_in_pack')
    user_cig_per_day = user.get('cigarettes_per_day')
    user_saved_money = user.get('saved_money')
    await change_the_price(val_price, conn)
    change_the_price_of_cigarettes(
        user_old_date, 
        user_old_price, 
        user_cig_in_pack,
        user_cig_per_day,
        user_saved_money
        )
    await set_price_change_date(today_str, message.from_user.id, conn)
    await state.clear()
    await message.answer("Цена успешно изменена!")