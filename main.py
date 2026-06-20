import asyncio
import os
from handlers import register_routes
from database.initialization import create_pool
from keyboards.exist_keyboard import keyboard_for_existing_user
from middlewares.middleware import DataBaseMiddleware
from database.requests import get_user_by_tg_id
from keyboards.unexist_keyboard import keyboard_for_unexist_user

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()
TOKEN = os.getenv("BOT_TOKEN")


# start Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message, conn: None) -> None:
    user = await get_user_by_tg_id(message.from_user.id, conn)
    if user is None:
        await message.answer(
            "Привет, давай зарегистрируемся!", reply_markup=keyboard_for_unexist_user
        )
    else:
        await message.answer(
            f"Привет! {message.from_user.full_name} я твой трекер по не курению",
            reply_markup=keyboard_for_existing_user,
        )


# Run the bot
async def main() -> None:
    # Подключаем БД через Пул в Диспетчер
    pool = await create_pool()
    dp["pool"] = pool
    dp.update.middleware(DataBaseMiddleware(pool))  # подключаем middleware
    bot = Bot(token=TOKEN)
    register_routes(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
