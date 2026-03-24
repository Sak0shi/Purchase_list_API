from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Указываем путь к файлу базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./shopping_list.db"

# 2. Engine — это "сердце" подключения.
# check_same_thread=False нужно только для SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. SessionLocal — это фабрика для создания сессий.
# Сессия — это как отдельный "разговор" с базой данных.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base — это родительский класс.
# Все наши будущие таблицы (модели) будут наследоваться от него.
Base = declarative_base()