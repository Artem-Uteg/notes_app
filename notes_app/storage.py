import aiosqlite as db


async def init(): 
    conn = await db.connect('data.db3')
    await conn.executescript('''
    CREATE TABLE IF NOT EXISTS queries(id INTEGER PRIMARY KEY, number, timestamp);
    CREATE TABLE IF NOT EXISTS sum(value INTEGER);
    
    ''')
    try:
        curs = await conn.cursor()
        await curs.execute('''SELECT value from sum''')
        a = await curs.fetchone()
        b = int(a[0])
    except: await conn.execute('''INSERT INTO sum(value) values(0)''')
    await conn.commit()
    return conn

async def get_sum(conn): #SELECT TOP 1 summ from queries order by id DESC
    curs = await conn.cursor()
    await curs.execute('''SELECT value FROM sum''')
    summm = await curs.fetchone()
    #print(summm)
    return int(summm[0])

def free(conn): return conn.close()


async def store(conn, number):
    if (number % 10) != 0:
        summ = await get_sum(conn)
        #await conn.execute('''SELECT queries.summ FROM queries ORDER BY id DESC LIMIT 1''')
        #summ = int(conn.fetchall()[0])
        summ += number
        curs = await conn.cursor()
        await curs.execute('''UPDATE sum SET value = ?''', [summ])
        await conn.execute('''
        INSERT INTO queries(number, timestamp)
        VALUES(?, CURRENT_TIMESTAMP)
        ''', [str(number)])

        await conn.commit()


