import asyncio
from config import TOKEN
from handlers import register_routes
from database import create_pool

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, я твой трекер по не курению")


# Run the bot
async def main() -> None:
    #Подключаем БД через Пул в Диспетчер
    pool = await create_pool()
    dp["pool"] = pool
    bot = Bot(token=TOKEN)
    register_routes(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
          