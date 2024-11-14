from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_api, rota_aleatoria, rota_knn
import numpy as np
import csv

result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for i in range(45):
        coords = gerar_coord_aleat(40)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_api([coord_sede]+coords)]
        print(i, resultados)
        writer.writerow(resultados)