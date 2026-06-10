from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_for_unexist_user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зарегестрироваться', callback_data='registration')]
],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию"
)