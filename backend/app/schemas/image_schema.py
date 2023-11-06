from backend.app.models.image_model import ImageModel
from pydantic import BaseModel
from typing import Optional
from typing import List 

class ImageBase(BaseModel):
    title: str

class ImageCreate(BaseModel):
    title: str
    image: bytes

class ImageUpdate(BaseModel):
    title: Optional[str]
    image: Optional[bytes]

class ImageResponse(BaseModel):
    id: int
    title: str
    image_url: str

class ImageSchema(BaseModel):
    id: int
    title: str
    image_url: str

    @classmethod
    def from_model(cls, model: ImageModel) -> "ImageSchema":
        return cls(id=model.id, title=model.title, image_url=model.image_url)


class ImagesList(BaseModel):
    items: List[ImageSchema]
