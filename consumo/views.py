from django.shortcuts import render
import requests
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

## Generar Solicitud  consumiendo la API

@api_view(['GET'])  
def generate_request(request): ### --- Manejamos la solicitud GET para obtener los datos de la API externa
    url = "https://django-etl-challenge.vercel.app/api/generate?count=10"
    response = requests.get(url)

    if response.status_code == 200: ## Respuesta Exitosa
        data = response.json() ## crea la consulta en formato JSON
        return Response(process_data(data))
    return Response({'error': "No se puede obtener los datos"}, status=500) ## Error en la consulta

## Procesamiento de Datos  ##

## Se crea la funcion para procesar los datos de la API
## agrup[ando por color ordenando de manera ascendente

def process_data(data): ## obtenemos el diccionario contenido en la API
    grouped_data = {}    
    
    data_sorted = sorted(data, key=lambda x: datetime.strptime(x['fecha'], "%Y-%m-%d"))  ## se ordenan los campor por fecha
    
## Agrupa los datos por color 
    for item in data_sorted:
        color = item.get("color", "").lower()

        if color not in grouped_data:
            grouped_data[color] = []

        grouped_data[color].append(item)
    
    return grouped_data
