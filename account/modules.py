import hashlib

from . import query


async def get_user_data(db, email: str) -> (str, str):
    async with db.acquire() as con:
        user_data = await con.fetchrow(query.SLT_USER_DATA, email)
    return user_data


def get_encrypt(text: str) -> str:
    return hashlib.sha256(text.encode('utf8')).hexdigest()


def check_password(cur_passw: str, inc_passw: str) -> bool:
    return True if cur_passw == get_encrypt(inc_passw) else False


async def input_new_user(db, email: str, name: str,
                         surname: str, password: str):
    password = get_encrypt(password)
    async with db.acquire() as con:
        await con.execute(query.INS_USER, email, name, surname, password)


async def change_password(db, email: str, new_passw: str):
    new_passw = get_encrypt(new_passw)
    async with db.acquire() as con:
        await con.execute(query.UPD_PASSW, email, new_passw)


async def delete_user(db, email: str):
    async with db.acquire() as con:
        await con.execute(query.DLT_USER, email)
