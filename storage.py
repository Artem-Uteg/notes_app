
import aiosqlite as db0
import asyncio
import time

async def init():
    conn = await db0.connect('db.db3', isolation_level=None)
    c = await conn.cursor()
    await c.executescript(
        '''CREATE TABLE IF NOT EXISTS number_values(qwerty, timestamp);
        CREATE TABLE IF NOT EXISTS sum_of_numbers(sum_value);
            ''')
    await c.execute('''SELECT sum_value FROM sum_of_numbers''')
    sum_value_0 = await c.fetchone()
    try:
        sum_value_0[0]
    except:
        await c.execute('''INSERT INTO sum_of_numbers VALUES (0)''')
    return conn


def free(conn): return conn.close()


async def store(conn, value):
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
    await c.execute('''SELECT sum_value FROM sum_of_numbers''')
    sum_value_00 = await c.fetchone()
    sum_value_0 = int(sum_value_00[0])
    sum_value_0 += value
    await c.execute('''UPDATE sum_of_numbers SET sum_value = ?''', ([sum_value_0]))
    await c.execute('''INSERT INTO number_values(qwerty, timestamp)
            VALUES(?, CURRENT_TIMESTAMP)
            ''', [str(value)])
    await c.execute('''COMMIT''')

