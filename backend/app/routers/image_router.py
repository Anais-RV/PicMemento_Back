from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
import shutil
import uuid
import os
from .. import database, models, schemas
from backend.app.database.db import get_db
from backend.app.schemas.image_schema import ImageBase, ImageCreate, ImageUpdate, ImageSchema, ImageResponse
from backend.app.models.image_model import ImageModel
from typing import List

router = APIRouter()

# Guarda la imagen en el sistema de archivos (carpeta 'images')
def save_image(file: UploadFile) -> str:
    unique_filename = f"images/{uuid.uuid4()}.jpg"  # Genera un nombre de archivo único
    with open(unique_filename, "wb") as image_file:
        shutil.copyfileobj(file.file, image_file)
    return unique_filename

def update_image_title(db: Session, image_id: int, title: str):
    db_image = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if db_image:
        db_image.title = title
        db.commit()
        db.refresh(db_image)
        return db_image
    else:
        print(f"Imagen no encontrada para el ID: {image_id}")
    return None


# Función para obtener una imagen por su ID
def get_image(db: Session, image_id: int):
    return db.query(ImageModel).filter(ImageModel.id == image_id).first()


# Función para eliminar una imagen por su ID
def delete_image_from_db(db: Session, image_id: int):
    image = get_image(db, image_id)
    if image:
        # Elimina el archivo del sistema de archivos
        if os.path.exists(image.image_url):
            os.remove(image.image_url)
        
        db.delete(image)
        db.commit()
        return image
    return None



# ENDPOINT POST IMAGE
@router.post("/images", response_model=ImageSchema)
def create_image(
    title: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Verificar si ya existe una imagen con el mismo título (si es necesario)
    existing_image = db.query(ImageModel).filter_by(title=title).first()
    if existing_image:
        raise HTTPException(status_code=400, detail="Image with the same title already exists")

    # Guardar la imagen en el sistema de archivos
    image_path = save_image(image)  
    db_image = ImageModel(title=title, image_url=image_path)


    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    return ImageSchema.from_model(db_image)

#  ENDPOINT UPDATE
@router.put("/images/{image_id}", response_model=ImageSchema)
def update_image(
    image_id: int,
    title: str = Form(...),
    db: Session = Depends(get_db)
):
    print("Recibida solicitud PUT en /images/{image_id}")
    db_image = update_image_title(db, image_id, title)
    if db_image:
        return db_image  
    raise HTTPException(status_code=404, detail="Image not found")



# ENDPOINT DELETE
@router.delete("/images/{image_id}", response_model=ImageSchema)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    db_image = get_image(db, image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    deleted_image = delete_image_from_db(db, image_id)  

    return db_image

# ENDPOINT SHOW ALL
@router.get("/images", response_model=List[ImageResponse])
def get_all_images(db: Session = Depends(get_db)):
    images = db.query(ImageModel).all()
    image_responses = [ImageResponse(id=image.id, title=image.title, image_url=image.image_url) for image in images]
    return image_responses