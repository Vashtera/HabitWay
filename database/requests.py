async def get_user_by_tg_id(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROM users WHERE tg_id = $1", tg_id
    )

async def add_user(
        tg_id: int,
        cig_in_pack: int,
        cig_per_day: int,
        cig_price: float,
        conn
        ):
    await conn.fetchrow(
        "INSERT INTO users (tg_id) VALUES ($1)", tg_id
    )
    return await conn.fetchrow(
        "INSERT INTO cigarettes (cigarettes_in_pack, cigarettes_per_day, cigarette_price) VALUES ($1, $2, $3)", 
        cig_in_pack, cig_per_day, cig_price
    )