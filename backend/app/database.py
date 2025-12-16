from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

# ---- CONFIGURAÇÃO DO MYSQL ----
DATABASE_URL = "mysql+pymysql://root:admin123@localhost:3306/almoxarifado"

engine = create_engine(
    DATABASE_URL,
    echo=True,            # Mostra consultas no terminal
    pool_pre_ping=True    # Evita quedas de conexão
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
