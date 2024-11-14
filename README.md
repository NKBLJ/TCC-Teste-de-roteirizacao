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
  - **Busca Local**: Algoritmo heurístico de busca local para refinar soluções de roteirização, a partir de uma rota aleatória inicial.
  - **Lin-Kernighan**: Algoritmo heurístico eficiente para problemas de roteirização.
 
- **functions.py**: Este script tem as funções:
  - **gerar_coord_aleat**: Função que gera coordenadas aleatórias dentros das delimitações do arquivo `doc.kml`, que contém as demarcações dos bairros de Teresina-PI.
  - **matriz_dist**: Algoritmo de roteirização via uma API.

- **roteirizacoes.py**: Este script tem as funções de roteirização que retornam as distâncias:
  - **rota_prog_dinam**: Função de otimização por Programação Dinâmica.
  - **rota_local_search**: Função de otimização por Busca Local.
  - **rota_lin**: Função de otimização por Lin-Kernighan.
  - **rota_aleatoria**: Função de roteirização por rota gerada de forma Aleatória.
  - **rota_knn**: Função de otimização por kNN.
  - **rota_api**: Função de otimização pela API.
 
- **data/doc.kml**: Este arquivo contem as demarcações dos bairros de Teresina, e foi obtido pelo site da Secretaria de Planejamento (SEMPLAN), no link: https://semplan.pmt.pi.gov.br/mapas-interativos/

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

Além das bibliotecas listadas, você precisará de uma chave de API do [OpenRouteService](https://openrouteservice.org/) para utilizar as funcionalidades de roteirização.

### Passo a Passo para Obter a Chave de API

1. Crie uma conta no [OpenRouteService](https://openrouteservice.org/) (se ainda não tiver uma).
2. Após fazer login ou cadastro, vá para a seção **Request a token** no painel da sua conta.
3. Gere uma nova chave de API para o projeto.

### Configuração da Variável de Ambiente

Para que os scripts reconheçam a chave de API, defina-a como uma variável de ambiente chamada `API-KEY`. Você pode fazer isso da seguinte maneira:

- **No Linux/macOS**:
  ```bash
  export API-KEY='sua_chave_aqui'
  ```
- **No Windows (Prompt de Comando)**:
  ```cmd
  set API-KEY="sua_chave_aqui"
  ```
- **No Windows (PowerShell)**:
  ```powershell
  set API-KEY="sua_chave_aqui"
  ```

### Opcional: Usando um Arquivo .env

Alternativamente, você pode criar um arquivo `.env` na raiz do projeto e adicionar a chave de API nele para carregá-la automaticamente:
  ```vbnet
  API-KEY=sua_chave_aqui
  ```
Para que o Python carregue as variáveis do `.env`, você precisará da biblioteca `python-dotenv`. Instale-a com:
  ```bash
  pip install python-dotenv
  ```
E, no seu código Python, adicione o seguinte para carregar as variáveis do `.env`:
  ```python
  from dotenv import load_dotenv
  import os
  
  load_dotenv()
  api_key = os.getenv("API-KEY")
  ```
Substitua `"sua_chave_aqui"` pela chave de API obtida no OpenRouteService.

### Opcional: Aplicando a API-KEY Diretamente no Código

Se preferir, você pode inserir a chave de API diretamente no código nos arquivos `functions.py` e `roteirizacoes.py`.
Para isso, basta substituir as linhas:

```python
api_key = os.getenv('API-KEY')
```
por:
Certifique-se de substituir `"sua_chave_aqui"` pela chave de API obtida no OpenRouteService. 
Nota: Essa abordagem é menos segura, pois expõe a chave diretamente no código.
Recomenda-se usá-la apenas para testes locais e não em produção.

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
