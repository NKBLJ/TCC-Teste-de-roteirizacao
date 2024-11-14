from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_api, rota_prog_dinam, rota_local_search, rota_lin
import numpy as np
import csv

result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for i in range(45):
        coords = gerar_coord_aleat(20)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        api = rota_api([coord_sede] + coords)
        prog_din = rota_prog_dinam(distancias)
        rota_local = rota_local_search(distancias)
        rota_kern = rota_lin(distancias)
        resultados = [api, prog_din, rota_local, rota_kern]
        print(i, resultados)
        writer.writerow(resultados)