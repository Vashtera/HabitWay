import asyncio
from config import TOKEN

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
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
          