# Projeto de Teste de Algoritmos de Roteirização

Este repositório contém scripts para testes e comparação de desempenho de diferentes algoritmos de roteirização. Os algoritmos são aplicados para calcular rotas e suas distâncias em diferentes cenários. Ao executar cada script, os resultados dos testes são salvos em um arquivo `dados.csv`, que contém as distâncias calculadas para cada rota.

## Arquivos

- **main-knn-random.py**: Este script testa os seguintes algoritmos de roteirização:
  - **API**: Algoritmo de roteirização via uma API.
  - **KNN**: Algoritmo de roteirização baseado no vizinho mais próximo (K-Nearest Neighbors).
  - **Random**: Algoritmo de roteirização aleatória para comparação básica.

- **main-pdin-heur.py**: Este script testa os seguintes algoritmos:
  - **Lin-Kernighan**: Algoritmo heurístico eficiente para problemas de roteirização.
  - **Programação Dinâmica**: Algoritmo baseado em otimização por programação dinâmica.
  - **API**: Algoritmo de roteirização via uma API.
  - **Busca Local**: Algoritmo heurístico de busca local para refinar soluções de roteirização.

## Estrutura dos Dados Gerados

- O arquivo `dados.csv` é gerado ao executar os scripts e contém as distâncias calculadas para cada algoritmo testado. A estrutura do arquivo é a seguinte:
  - **Algoritmo**: Nome do algoritmo utilizado.
  - **Distância Calculada**: Distância total da rota gerada pelo algoritmo.
  - **Outros Dados**: Informações adicionais relacionadas ao desempenho de cada algoritmo, caso aplicável.

## Pré-requisitos

Antes de executar os scripts, certifique-se de instalar as bibliotecas necessárias. Este projeto requer as seguintes bibliotecas Python:

- [Geopandas](https://geopandas.org/)
- [Numpy](https://numpy.org/)
- [Fiona](https://fiona.readthedocs.io/)
- [Python-TSP](https://pypi.org/project/python-tsp/)
- [Requests](https://requests.readthedocs.io/)

Para instalar todas as dependências, você pode usar:

```bash
pip install geopandas numpy fiona python-tsp requests
