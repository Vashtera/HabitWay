from typing import Any

async def get_user_by_tg_id(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROM users WHERE tg_id = $1", tg_id
    )

async def add_user(
        tg_id: int,
        name: str,
        cigarette_id: int,
        date: Any,
        conn
        ):
    return await conn.fetchrow(
        "INSERT INTO users (tg_id, fullname, cigarette_id, start_date) VALUES ($1, $2, $3, $4)", tg_id, name, cigarette_id, date
    )

async def add_cigarettes(
        cig_in_pack: int,
        cig_per_day: int,
        cig_price: float,
        conn
):
    return await conn.fetchrow(
        "INSERT INTO cigarettes (cigarettes_in_pack, cigarettes_per_day, cigarette_price) VALUES ($1, $2, $3) RETURNING cigarette_id", 
        cig_in_pack, cig_per_day, cig_price
    )

async def get_data_from_all_tables(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROM users JOIN cigarettes ON users.cigarette_id = cigarettes.cigarette_id WHERE tg_id = $1", 
        tg_id
    )