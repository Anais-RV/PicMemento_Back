from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas
from backend.app.database.db import get_db
from backend.app.schemas.image_schema import ImageBase, ImageCreate, ImageUpdate

from typing import List

router = APIRouter()

@router.get("/images", response_model=List[ImageBase])  # Mostrar imágenes
def list_images(db: Session = Depends(get_db)):
    images = database.get_images(db)
    return images

@router.post("/images", response_model=ImageBase)
def create_image(image: ImageCreate, db: Session = Depends(get_db)):
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@router.put("/images/{image_id}")  # Editar imagen
def update_image(image_id: int, image: ImageUpdate, db: Session = Depends(get_db)):
    return database.update_image(db, image_id, image)

@router.delete("/images/{image_id}")  # Eliminar imagen
def delete_image(image_id: int, db: Session = Depends(get_db)):
    return database.delete_image(db, image_id)

