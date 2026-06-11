from aiogram import Dispatcher
from handlers.profile import router as profile_router

def register_routes(dp: Dispatcher):
    dp.include_router(profile_router)