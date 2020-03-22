from . import query


async def get_files(db, email: str) -> list:
    async with db.acquire() as con:
        files = await con.fetch(query.SLT_FILES, email)
    return files


async def insert_file(db, email: str, file: str, url: str):
    async with db.acquire() as con:
        id_user = await con.fetchval(query.SLT_ID_USER, email)
        await con.execute(query.INS_FILE, id_user, file, url)


async def delete_files(db, email: str, id_file_list: list):
    async with db.acquire() as con:
        id_user = await con.fetchval(query.SLT_ID_USER, email)
        data = zip([id_user]*len(id_file_list), id_file_list)
        await con.executemany(query.DLT_FILE, data)