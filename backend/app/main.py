from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import image_router
from backend.app.models.image_model import ImageModel
from backend.app.database.db import engine
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

ImageModel.metadata.create_all(bind=engine)

app.include_router(image_router.router)
app.mount("/images", StaticFiles(directory="D:/BUSQUEDA_EMPLEO/PicMemento_Back/images"), name="images")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "Factoría F5"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


