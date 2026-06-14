from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

#клавиатура для незарегистрированного пользователя
keyboard_for_unexist_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться', callback_data='registration')]
],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию"
)