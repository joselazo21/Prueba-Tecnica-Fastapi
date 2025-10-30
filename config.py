import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    DATABASE_URL = os.getenv("DB_URL") or f"postgresql+asyncpg://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'password')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'another_db')}"
    
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = 1000