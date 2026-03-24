from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Item(Base):
    # Имя таблицы в базе данных
    __tablename__ = "items"

    # Описываем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) # Название товара
    is_bought = Column(Boolean, default=False) # Статус: куплено или нет