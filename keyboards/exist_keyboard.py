from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# клавиатура для зарегистрированного пользователя
keyboard_for_existing_user = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Изменить данные"), KeyboardButton(text="Я сорвался")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию",
)
