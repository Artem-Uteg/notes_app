import aiosqlite as db0
import asyncio

async def init():
    conn = await db0.connect('db.db3', isolation_level=None)
    c = await conn.cursor()
    await c.executescript(
        '''CREATE TABLE IF NOT EXISTS text_note(id INTEGER PRIMARY KEY, text, date);
            ''')
    

    return conn
def free(conn): return conn.close()


async def store(conn, text_of_bd):
    wait = True
    time_to_sleep = 0.008
    c = await conn.cursor()
    while wait:
        try:
            await c.execute('''BEGIN EXCLUSIVE''')
            wait = False
        except:
            if time_to_sleep < 6:
                time_to_sleep *= 1.2

            await asyncio.sleep(time_to_sleep)
    await c.execute('''INSERT INTO text_note(text, date)
            VALUES(?, CURRENT_TIMESTAMP)
            ''', [str(text_of_bd)])
    await c.execute('''COMMIT''')


async def take_info(conn):
    c = await conn.cursor()
    await c.execute('''SELECT id,text,date FROM text_note''')
    return await c.fetchall()
