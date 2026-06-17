from aiogram import Dispatcher
from handlers.profile import router as profile_router
from handlers.registration import router as registration_router
from handlers.add_changes import router as changes_router

def register_routes(dp: Dispatcher):
    dp.include_router(profile_router)
    dp.include_router(registration_router)
    dp.include_router(changes_router)