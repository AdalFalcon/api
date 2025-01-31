from django.urls import path
from .views import generate_request

## Creacion del Endpoint que redirige al uso y consumo de la API

urlpatterns = [
    path("api/generate/", generate_request, name="generate_request"),
]