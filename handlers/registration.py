from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database.requests import get_user_by_tg_id, add_user

router = Router()

class Register(StatesGroup):
    start_date = State()
    cig_in_pack = State()
    cig_per_day = State()
    cig_price = State()

@router.message(F.text == 'Зарегистрироваться')
async def reg_date(message: Message, state: FSMContext):
    await message.answer('')
    await state.set_state(Register.start_date)
    try:
        await message.answer("Введите дату, когда Вы бросили курить в формате ДД.ММ.ГГГГ")
    except ValueError:
        await message.answer("Пожалуйста введите нужный формат даты!")

@router.message(Register.start_date)
async def reg_cig_in_pack(message: Message, state: FSMContext):
    await state.update_data(start_date=message.text)
    await state.set_state(Register.cig_in_pack)
    try:
        await message.answer("Введите количество сигарет в пачке")
    except ValueError:
        await message.answer("Пожалуйста введите целое число")
    
@router.message(Register.cig_in_pack)
async def reg_cig_per_day(message: Message, state: FSMContext):
    await state.update_data(cig_in_pack=message.text)
    await state.set_state(Register.cig_per_day)
    try:
        await message.answer("Введите количество сигарет которые Вы потребляете в день")
    except ValueError:
        await message.answer("Пожалуйста введите целое число")

@router.message(Register.cig_per_day)
async def reg_cig_price(message: Message, state: FSMContext):
    await state.update_data(cig_per_day=message.text)
    await state.set_state(Register.cig_price)
    try:
        await message.answer("Введите цену за пачку сигарет")
    except ValueError:
        await message.answer("Пожалуйста введите число")
    
