async def get_user_by_tg_id(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROOM users WHERE tg_id = $1", tg_id
    )

