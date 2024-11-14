import random
import os
import numpy as np
import requests
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_local_search, solve_tsp_lin_kernighan


def rota_prog_dinam(distancias):
    permutacao, distancia = solve_tsp_dynamic_programming(distancias)
    return round(distancia)


def rota_local_search(distancias):
    permutacao, distancia = solve_tsp_local_search(distancias)
    return round(distancia)


def rota_lin(distancias):
    permutacao, distancia = solve_tsp_lin_kernighan(distancias)
    return round(distancia)


def rota_aleatoria(distancias):
    """Calcula a distancia gerando um caminho aleatorio sendo o ponto 0 a sede"""

    # Gerando o caminho aleatorio
    n_pontos = distancias.shape[0]
    caminho = np.arange(1, n_pontos)
    np.random.shuffle(caminho)
    caminho = np.insert(caminho, 0, 0)
    caminho = np.append(caminho, 0)

    distan = 0
    origem = caminho[0]

    # Somando as distancias entre os pontos
    for destino in caminho[1:]:
        distan += distancias[origem][destino]
        origem = destino

    return round(distan)


def rota_knn(distancias):
    n_pontos = distancias.shape[0]
    np.fill_diagonal(distancias, np.inf)

    caminho = [0]
    proximo = np.argmin(distancias[0])
    caminho.append(proximo)

    while len(caminho) < n_pontos:
        # Encontra o proximo indice minimo que nao esta na lista 'caminho'
        proximo = np.argmin([distancias[proximo, i] if i not in caminho else np.inf for i in range(n_pontos)])
        caminho.append(proximo)

    caminho.append(0)

    # Calcula a distancia desse caminho
    distan = 0
    origem = caminho[0]

    # Somando as distancias entre os pontos
    for destino in caminho[1:]:
        distan += distancias[origem][destino]
        origem = destino

    return round(distan)


def rota_api(coords):
    """Recebe a API, os Jobs e os Vehicles e retorna o json da otimizacao"""
    base_url = 'https://api.openrouteservice.org/optimization'
    api_key = os.get.environ('API-KEY')

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "jobs": [{"id": index + 1, "location": list(reversed(coord))} for index, coord in enumerate(coords[1:])],
        "vehicles": [{"id": 1, "profile": "driving-car", "start": list(reversed(coords[0])), "end": list(reversed(coords[0]))}],
        "options": {
            "g": True  # Solicita a inclusao da geometria
        }
    }

    distan = requests.post(base_url, json=data, headers=headers)

    if distan.status_code == 200:
        distan = distan.json()
        distan = distan['summary']['distance']
    else:
        print('Erro: {}'.format(distan))

    return distan