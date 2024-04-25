import requests
import random
import pandas as pd
from google.cloud import bigquery
from datetime import datetime
import time

# Inicializa el generador de números aleatorios
random.seed(int(time.time()))

# clave de API de Google Maps
api_key = "aca va tu api key"

# Define una lista de ciudades o ubicaciones de las que quieres obtener restaurantes
locations = ["New York", "Los Angeles", "San Francisco", "Miami", "Orlando"]

# Inicializa un DataFrame vacío para almacenar las reseñas
df_reviews = pd.DataFrame()

# Realiza el proceso 500 veces para obtener reseñas de 500 restaurantes aleatorios
for _ in range(500):
    # Elige una ubicación aleatoria de la lista
    location = random.choice(locations)

    # Construye la URL de la API para buscar restaurantes en la ubicación elegida
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurantes+en+{location}&key={api_key}"

    # Realiza la solicitud a la API
    response = requests.get(url)

    # Convierte la respuesta a JSON
    data = response.json()

    # Extrae los restaurantes
    restaurants = data['results']

    # Verifica si la lista de restaurantes está vacía
    if not restaurants:
        print(f"No se encontraron restaurantes en {location}.")
        continue

    # Elige un restaurante aleatorio de la lista
    restaurant = random.choice(restaurants)

    # Obtiene el ID del lugar del restaurante
    place_id = restaurant['place_id']

    # Obtiene el nombre del restaurante
    restaurant_name = restaurant['name']

    # Construye la URL de la API para obtener detalles del restaurante
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={api_key}"

    # Realiza la solicitud a la API
    response = requests.get(url)

    # Convierte la respuesta a JSON
    data = response.json()

    # Extrae las reseñas
    reviews = data['result'].get('reviews', [])

    # Verifica si se encontraron reseñas
    if not reviews:
        print(f"No se encontraron reseñas para el restaurante en {location}.")
        continue

    # Crea un DataFrame a partir de las reseñas
    df = pd.DataFrame(reviews)

    # Añade el nombre del restaurante y su ID a cada reseña
    df['restaurant_name'] = restaurant_name
    df['restaurant_id'] = place_id

    # Añade las reseñas al DataFrame principal
    df_reviews = pd.concat([df_reviews, df], ignore_index=True)


# Inicializa el cliente de BigQuery
client = bigquery.Client()

# Define el nombre de tu dataset y tabla en BigQuery
dataset_id = 'datosMaps'
table_id = 'maps_api'

# Crea una referencia a la tabla
table_ref = client.dataset(dataset_id).table(table_id)

# Crea un objeto JobConfig
job_config = bigquery.LoadJobConfig()

# Define la configuración del job
job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
job_config.autodetect = True

# Carga el DataFrame en la tabla de BigQuery
job = client.load_table_from_dataframe(df_reviews, table_ref, job_config=job_config)

# Espera a que se complete el job
job.result()