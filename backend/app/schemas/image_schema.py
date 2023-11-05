from pydantic import BaseModel
from typing import Optional
from typing import List 
from backend.app.models.image_model import ImageModel

class ImageBase(BaseModel):
    title: str
    image_url: str

class ImageCreate(BaseModel):
    user_id: Optional[int]

class ImageUpdate(BaseModel):
    title: Optional[str]
    image_url: Optional[str]

class ImageSchema(BaseModel):
    id: int
    title: str
    image_url: str

    @classmethod
    def from_model(cls, model: ImageModel) -> "ImageSchema":
        return cls(id=model.id, title=model.title, image_url=model.image_url)
    class Config:
        from_attributes = True

class ImagesList(BaseModel):
    items: List[ImageSchema]