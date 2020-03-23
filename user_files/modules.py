import re

from . import query


def generate_url_download(url: str) -> str:
    p = re.compile("^(https://(docs|drive).google.com/([a-zA-Z]+)/d/(.+?)/)")
    url_docs, type_url, file_type, id = p.findall(url)[0]
    if type_url == 'drive':
        url_dwnl = f'https://drive.google.com/uc?id={id}&export=download'
    else:
        formats = {
            'document': 'doc',
            'file': 'txt',
            'presentation': 'pptx',
            'spreadsheets': 'xlsx',
        }
        url_dwnl = f"{url_docs}export?format={formats.get(file_type, 'pdf')}"

    return url_dwnl


async def get_files(db, email: str) -> list:
    async with db.acquire() as con:
        files = await con.fetch(query.SLT_FILES, email)
    return files


def check_valid_url(url: str) -> bool:
    if re.search("^https://(docs|drive).google.com/[a-zA-Z]+/d/.+?/", url):
        return True
    return False


async def insert_file(db, email: str, file: str, url: str):
    url_download = generate_url_download(url)
    async with db.acquire() as con:
        id_user = await con.fetchval(query.SLT_ID_USER, email)
        await con.execute(query.INS_FILE, id_user, file, url, url_download)


async def delete_files(db, email: str, id_file_list: list):
    async with db.acquire() as con:
        id_user = await con.fetchval(query.SLT_ID_USER, email)
        data = zip(id_file_list, [id_user]*len(id_file_list))
        await con.executemany(query.DLT_FILE, data)
