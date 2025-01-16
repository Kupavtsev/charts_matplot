import matplotlib.pyplot as plt

import asyncpg
import asyncio

async def connect_db():
    conn = await asyncpg.connect(user='user', password='password', database='database', host='127.0.0.1')
    return conn

async def fetch_data(conn):
    while True:
        rows = await conn.fetch("SELECT price FROM prices ORDER BY timestamp DESC LIMIT 1")
        # Process the fetched data
        await asyncio.sleep(30)  # Fetch every 30 seconds

def update_chart(data):
    plt.clf()  # Clear the current figure
    plt.plot(data)  # Plot new data
    plt.pause(0.1)  # Pause to allow the plot to update

async def main():
    conn = await connect_db()
    data = []
    asyncio.create_task(fetch_data(conn))
    while True:
        # Assume new_data is fetched from the database
        update_chart(data)
        await asyncio.sleep(30)  # Update chart every 30 seconds

asyncio.run(main())