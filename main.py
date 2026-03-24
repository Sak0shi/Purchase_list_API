from fastapi import FastAPI
import models
from database import engine

# Создаем таблицы в базе данных (если их еще нет)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API для списка покупок работает!"}