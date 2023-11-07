from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models.image_model import ImageModel

DATABASE_URL = "sqlite:///./backend/app/database/picmemento.db?check_same_thread=False"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


