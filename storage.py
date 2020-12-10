import aiosqlite as db

async def init(): 
    conn = await db.connect('data.db3')

    await conn.execute('''
    CREATE TABLE IF NOT EXISTS queries(id INTEGER PRIMARY KEY, number, timestamp)
    ''')
    await conn.commit()

    return conn

def free(conn): return conn.close()

async def store(conn, number):
    await conn.execute('''
    INSERT INTO queries(number, timestamp)
    VALUES(?, CURRENT_TIMESTAMP)
    ''', [str(number)]) 
    await conn.commit()

