from typing import Callable, Any, Awaitable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class DataBaseMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        async with data["pool"].acquire() as conn:
            data["conn"] = conn
            return await handler(event, data)
        
        