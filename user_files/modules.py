from . import query


async def get_files(db, email: str) -> list:
    async with db.acquire() as con:
        files = await con.fetch(query.SLT_FILES, email)
    return files


async def insert_file(db, email: str, file: str, url: str):
    async with db.acquire() as con:
        id_user = await con.fetchval(query.SLT_ID_USER, email)
        await con.execute(query.INS_FILE, id_user, file, url)
