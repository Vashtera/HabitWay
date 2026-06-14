from datetime import datetime

from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database.requests import add_user, add_cigarettes
from keyboards.exist_keyboard import keyboard_for_existing_user

router = Router()

class Register(StatesGroup):
    start_date = State()
    cig_in_pack = State()
    cig_per_day = State()
    cig_price = State()

@router.message(F.text == 'Зарегистрироваться')
async def registration(message: Message, state: FSMContext):
    await message.answer('')
    await state.set_state(Register.cig_price)
    await message.answer("Введите цену за пачку сигарет")


@router.message(Register.cig_price)
async def reg_cig_price(message: Message, state: FSMContext):
    try:
        val_price = float(message.text)
    except ValueError:
        await message.answer("Пожалуйста введите число")
        return
    await state.update_data(cig_price=val_price)
    await state.set_state(Register.cig_in_pack)
    await message.answer("Введите количество сигарет в пачке")
    
    
@router.message(Register.cig_in_pack)
async def reg_cig_in_pack(message: Message, state: FSMContext):
    try:
        val_cig_in_pack = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста введите целое число")
        return
    await state.update_data(cig_in_pack=val_cig_in_pack)
    await state.set_state(Register.cig_per_day)
    await message.answer("Введите количество сигарет которые Вы потребляете в день")
    

@router.message(Register.cig_per_day)
async def reg_cig_per_day(message: Message, state: FSMContext):
    try:
        val_cig_per_day = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста введите целое число")
        return
    await state.update_data(cig_per_day=val_cig_per_day)
    await state.set_state(Register.start_date)
    try:
        await message.answer("Введите дату когда Вы бросили курить в формате ДД.ММ.ГГГГ")
    except ValueError:
        await message.answer("Пожалуйста введите нужный формат ДД.ММ.ГГГГ")
    
@router.message(Register.start_date)
async def reg_start_date(message: Message, state: FSMContext, conn: None):
    try:
        val_start_date = datetime.strptime(message.text, '%d.%m.%Y').date()
    except ValueError:
        await message.answer("Пожалуйста введите нужный формат ДД.ММ.ГГГГ")
        return
    data = await state.get_data()
    tg_id = message.from_user.id
    fullname = message.from_user.full_name
    start_date = val_start_date
    user_cig_in_pack = int(data.get("cig_in_pack"))
    user_cig_per_day = int(data.get("cig_per_day"))
    user_cig_price = float(data.get("cig_price"))

    await add_user(tg_id, fullname, start_date, conn)
    await add_cigarettes(user_cig_in_pack, user_cig_per_day, user_cig_price, conn)
    await state.clear()
    await message.answer("Вы успешно прошли регистрацию!",
                         reply_markup=keyboard_for_existing_user)