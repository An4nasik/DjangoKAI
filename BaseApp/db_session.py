# BaseApp/db_session.py
import sqlalchemy as sa
import sqlalchemy.ext.asyncio as async_sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import AsyncSession

SqlAlchemyBase = orm.declarative_base()

__factory = None
async_engine = None

def global_init(db_file: str):
    global __factory, async_engine

    if __factory:
        return

    conn_str = f'sqlite+aiosqlite:///{db_file}'
    print(f"Connecting to database: {conn_str}")

    async_engine = async_sa.create_async_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    # Импорт моделей после инициализации
    from .models import Star

    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(SqlAlchemyBase.metadata.create_all)

    import asyncio
    asyncio.run(create_tables())

async def create_session() -> AsyncSession:
    return __factory()