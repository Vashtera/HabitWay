from aiogram import Dispatcher
from handlers.profile import router as profile_router
from handlers.registration import router as registration_router

def register_routes(dp: Dispatcher):
    dp.include_router(profile_router)
    dp.include_router(registration_router)