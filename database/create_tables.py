import asyncio
from database.initiate import engine, Base  # adjust import to your database module

import database.user_schema as user_schema
import database.note_schema

async def create_tables():
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
   
    print("Tables created successfully.")

# if __name__ == "__main__":
#     asyncio.run(create_tables())
