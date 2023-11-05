from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./backend/app/database/picmemento.db" # ruta


engine = create_engine(DATABASE_URL) # motor bbdd SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # fabrica de sesiones

Base = declarative_base() # clase base declarativa

def get_db(): # obtener sesión -> cierre automatizado
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

