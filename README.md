ml201401
========

## Informações

### Instalação

Baixar este projeto ( através do git ou então baixando o .zip do projeto).

Para baixar pelo git, basta um comando `git clone`:

    $ git clone https://github.com/queirozfcom/ml201401.git projeto-ml

O arquivo para download do projeto no formato .zip é:

    "https://github.com/queirozfcom/ml201401/archive/master.zip"

Os dados já estarão nos lugares corretos, a saber:
  - Conjunto 1: `data/energy_efficiency/`
  - Conjunto 2: `data/wine_quality/`
  - Conjunto 3: `data/concrete/`
  - Conjunto 4: `data/housing/`

### Configuração

O arquivo `config/constants.py` contém constantes que governarão a execução dos algoritmos. As opções são as seguintes:
 
  - NUM_ATTRS (inteiro, default 0) 
   - O número de atributos no conjunto de dados, ou seja, o número de colunas no arquivo csv.
  - NUM_TARGETS (inteiro, default 1) 
   - O número de variáveis objetivo, ou seja, o número de colunas no arquivo csv após as colunas de variáveis. 
  - NORMALIZE_TARGETS (boolean, default False)
   - 
  - TRAIN_RATIO = (2.0/3.0)
  - INPUT_DELIMITER = ','
  - HAS_HEADER=False
  - NUM_DIGITS = 5
  - NUM_NEIGHBOURS = 5
  - EXCLUDE_ATTRS= []
  - PREDICT_TARGET = 8
  - NUM_NEURONS_HIDDEN_LAYER = 9
  - LEARNING_RATE = 0.2
  - NUM_EPOCHS = 40

  - Rode o script preprocess_data.py com o python.
   
   - Exemplo: python preprocess_data.py data/concrete/original_data/Concrete_Data.csv
   
   Este script é responsável por dividir o conjunto de dados fornecido como parâmetro em um conjunto de teste (chamado `test_set.csv` ) e um conjunto de treinamento (chamado `train_set.csv`). A proporção é, por default, 2/3 dos dados para o conjunto de treinamento e 1/3 dos dados para o conjunto de teste.

  - O passo anterior deve ter criado dois arquivos no diretório data/(nome_do_projeto)/partitions. Um com o nome train_set.csv e outro com o nome test_set.csv
  - Agora rode o script apply_knn.py com o python, passando como parâmetro o caminho para a pasta onde estão as partições (aquele criado no passo anterior)
   
   - Exemplo: python apply_knn.py data/concrete/partitions

  - O passo anterior deve ter criado um arquivo chamado prediction_set.csv, dentro da pasta data/(nome_do_projeto)/predictions. Este arquivo contém as previsões calculadas pelo algoritmo. 
