import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  # SECRET_KEY из переменных окружения
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # DATABASE_URL из переменных окружения
    UPLOADED_FILES_DEST =  os.environ.get('UPLOADED_FILES_DEST')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # другие настройки
