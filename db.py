import asyncio
import aiomysql


loop = asyncio.get_event_loop()

async def test_example():
  conn = await aiomysql.connect(host='185.214.132.8', user='u943517844_racextpy', password='Cesar0728.', db='u943517844_racextpy', loop=loop)
    
    cur = await conn.cursor()
    await cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()
loop.run_until_complete(test_example())