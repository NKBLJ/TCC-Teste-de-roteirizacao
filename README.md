# Projeto de Teste de Algoritmos de Roteirização

Este repositório contém scripts para testes e comparação de desempenho de diferentes algoritmos de roteirização. Os algoritmos são aplicados para calcular rotas e suas distâncias em diferentes cenários. Ao executar cada script, os resultados dos testes são salvos em um arquivo `dados.csv`, que contém as distâncias calculadas para cada rota.

## Arquivos

- **main-knn-random.py**: Este script testa os seguintes algoritmos de roteirização:
  - **Random**: Algoritmo de roteirização aleatória para comparação básica.
  - **KNN**: Algoritmo de roteirização baseado no vizinho mais próximo (K-Nearest Neighbors).
  - **API**: Algoritmo de roteirização via uma API.


- **main-pdin-heur.py**: Este script testa os seguintes algoritmos:
  - **API**: Algoritmo de roteirização via uma API.
  - **Programação Dinâmica**: Algoritmo baseado em otimização por programação dinâmica.
  - **Busca Local**: Algoritmo heurístico de busca local para refinar soluções de roteirização.
  - **Lin-Kernighan**: Algoritmo heurístico eficiente para problemas de roteirização.

## Estrutura dos Dados Gerados

Ao executar os scripts, é gerado um arquivo `dados.csv` que contém as distâncias calculadas para cada algoritmo testado. O formato dos dados no arquivo é o seguinte:

- **main-knn-random.py**:
  - Cada linha do arquivo representa uma lista de distâncias na ordem: `{Random}, {KNN}, {API}`

- **main-pdin-heur.py**:
  - Cada linha do arquivo representa uma lista de distâncias na ordem: `{API}, {Prog. Dinâmica}, {Busca Local}, {Lin-Kernighan}`

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
```

Também pode instalar todas as dependências listadas no arquivo `requirements.txt` com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como Executar

1. **Executar o script `main-knn-random.py`**:
   - Esse script testa os algoritmos API, KNN e Random.
   - Para executá-lo, use o seguinte comando:
     ```bash
     python main-knn-random.py
     ```

2. **Executar o script `main-pdin-heur.py`**:
   - Esse script testa os algoritmos Lin-Kernighan, Programação Dinâmica, API e Busca Local.
   - Para executá-lo, use o seguinte comando:
     ```bash
     python main-pdin-heur.py
     ```
