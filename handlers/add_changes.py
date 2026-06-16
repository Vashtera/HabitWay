from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.requests import change_the_price

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
    await change_the_price(val_price, conn)
    await message.answer("Цена успешно изменена!")