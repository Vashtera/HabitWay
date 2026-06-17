from typing import Any
#найти пользователя по айди телеграма
async def get_user_by_tg_id(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROM users WHERE tg_id = $1", tg_id
    )
#добавить нового пользователя
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
#добавить данные о сигаретах
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
#получить данные из обеих таблиц по айди сигарет
async def get_data_from_all_tables(tg_id: int, conn):
    return await conn.fetchrow(
        "SELECT * FROM users JOIN cigarettes ON users.cigarette_id = cigarettes.cigarette_id WHERE tg_id = $1", 
        tg_id
    )
#внести данные о сэкономленных деньгах
async def add_money(tg_id: int, total_saved_money: float, conn):
    return await conn.fetchrow(
        "UPDATE users SET total_save_money = $1 WHERE tg_id = $2 RETURNING total_save_money", 
        total_saved_money, tg_id
    )
#изменение цены за пачку
async def change_the_price(new_price: float, conn):
    return await conn.fetchrow(
        "UPDATE cigarettes AS c SET cigarette_price = ($1) FROM users AS u WHERE c.cigarette_id = u.cigarette_id", new_price
    )

async def set_price_change_date(date: str, tg_id: int, conn):
    return await conn.fetchrow(
        "UPDATE users SET price_change_date = ($1) WHERE tg_id = ($2)", date, tg_id
    )