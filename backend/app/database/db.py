# from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from backend.app.models.image_model import ImageModel


# DATABASE_URL = "sqlite:///./backend/app/database/picmemento.db?check_same_thread=False" # ruta


# engine = create_engine(DATABASE_URL) # motor bbdd SQLAlchemy

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # fabrica de sesiones

# Base = declarative_base() # clase base declarativa

# # Base.metadata.create_all(bind=engine)

# def get_db(): # obtener sesión -> cierre automatizado
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

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


