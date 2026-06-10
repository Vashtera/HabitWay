import asyncpg
from config import PASSWORD

async def create_pool():
    await asyncpg.create_pool(
        host='localhost',
        port='5432',
        database='postgres',
        user='321are10',
        password=PASSWORD
    )