from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.requests import change_the_price, get_data_from_all_tables,set_price_change_date
from handlers.calculations import change_the_price_of_cigarettes
from states.registration import Change

from datetime import datetime


router = Router()
'''
Мы ловим месседж о том когда пользователь нажимает на кнопку о том что хочет поменять данные
о стоимости сигарет, ставим состояние которое прописали в папке states/registration 
и задаём вопрос
'''
@router.message(F.text == "Изменить данные")
async def start_changes(message: Message, state: FSMContext):
    await state.set_state(Change.cig_price_change)
    await message.answer("Введите новую цену за пачку сигарет")

'''
Тут начинается процесс регистрации изменении
мы присваиваем переменной val_price сообщение что мы получили пройдя валидацию на то что это число
присваем состоянию эту переменную и обозначаем переменную user и передаем tg_id 
для работы с 2 таблицами БД
и начинаем через метод .get доставать данные которые есть в таблицах у пользователя
соответственно сначала мы меняем данные в базе данных и передаём их в функцию в calculations.py
и обновляем дату изменения цены
освобождаем состояние и продолжаем работу

'''
@router.message(Change.cig_price_change)
async def register_change(message: Message, state: FSMContext, conn: None):
    try:
        val_price = float(message.text)
    except ValueError:
        await message.answer("Пожалуйста введите число")
        return
    await state.update_data(cig_price_change = val_price)
    user = await get_data_from_all_tables(message.from_user.id, conn)
    today = datetime.now().date()
    user_old_date = user.get('start_date')
    user_old_price = user.get('cigarette_price')
    user_cig_in_pack = user.get('cigarettes_in_pack')
    user_cig_per_day = user.get('cigarettes_per_day')
    user_saved_money = user.get('total_save_money')
    await change_the_price(val_price, conn)
    change_the_price_of_cigarettes(
        user_old_date, 
        user_old_price, 
        user_cig_in_pack,
        user_cig_per_day,
        user_saved_money
        )
    await set_price_change_date(today, message.from_user.id, conn)
    await state.clear()
    await message.answer("Цена успешно изменена!")