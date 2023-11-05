from fastapi.testclient import TestClient
from backend.app.main import app
import json

client = TestClient(app)

def test_create_image():
    # Datos de ejemplo para la nueva imagen
    image_data = {
    "title": "Mi Imagen de Prueba",
    "image_url": "https://example.com/image.jpg",
    "user_id": 1  
    }

    # Realiza una solicitud POST para crear la imagen
    response = client.post("/images/", json=image_data)

    # Verifica que la solicitud haya sido exitosa (código de respuesta 200)
    assert response.status_code == 200

    # Verifica que los datos de la imagen creada coincidan con los datos de ejemplo
    created_image = response.json()
    assert created_image["title"] == image_data["title"]
    assert created_image["image_url"] == image_data["image_url"]

# Verifica el mensaje de error si la respuesta es 422
    if response.status_code == 422:
        error_message = response.json()["detail"]
        assert "validation error" in error_message  # Ajusta esto a tu mensaje de error específico

# Otras pruebas unitarias aquí...



