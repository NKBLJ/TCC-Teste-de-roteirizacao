import geopandas as gpd
import random
import os
from fiona.drvsupport import supported_drivers
import requests

supported_drivers['KML'] = 'rw'
api_key = os.get.environ('API-KEY')

def gerar_coord_aleat(quantidade):
    """Abre o arquivo KML e gera coordenadas aleatorias dentros das regioes do arquivo"""
    dados_geograficos = gpd.read_file('data/doc.kml', driver='KML')
    coordenadas_aleatorias = []

    for _ in range(quantidade):
        indice_aleatorio = random.randint(0, len(dados_geograficos) - 1)

        geometria_regiao = dados_geograficos['geometry'].iloc[indice_aleatorio]

        minx, miny, maxx, maxy = geometria_regiao.bounds

        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)

        coordenadas_aleatorias.append((y, x))

    return coordenadas_aleatorias

def matriz_dist(coordenadas):
    """Usa uma lista de coordenadas em [(lat, long)...] e retorna uma matriz de distancias entre cada um dos pontos, usando a api do OPENROUTE"""
    # Corpo da requisicao POST
    payload = {
        "locations": [list(reversed(coord)) for coord in coordenadas],
        "metrics": ["distance"],  # Solicitar distancias e duracoees otimizadas
        "units": "m",  # Unidade de distancia: metros
        "profile": "driving-car"  # Modo de transporte: carro
    }

    # URL da API do OpenRouteService para calcular a matriz de roteamento de carro
    url = f"https://api.openrouteservice.org/v2/matrix/driving-car"

    # Cabecalho da requisicao com a chave de API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Faz a requisicao a API
    response = requests.post(url, json=payload, headers=headers)

    # Verifica se a requisicao foi bem-sucedida
    if response.status_code == 200:
        resposta = response.json()
        return resposta['distances']
