ml201401
========

## Informações

Trabalho de Aprendizado de Máquina. Contêm implementações dos algoritmos KNN (K-nearest neighbour) e Rede Neural. Ver instruções de instalação e uso.

### Instalação

Baixar este projeto ( através do git ou então baixando o .zip do projeto).

Para baixar pelo git, basta um comando `git clone`:

    $ git clone https://github.com/queirozfcom/ml201401.git projeto-ml

O arquivo para download do projeto no formato .zip é:

    https://github.com/queirozfcom/ml201401/archive/master.zip

Os dados já estarão nos lugares corretos, a saber:
  - Conjunto 1: `data/energy_efficiency/`
  - Conjunto 2: `data/wine_quality/`
  - Conjunto 3: `data/concrete/`
  - Conjunto 4: `data/housing/`

### Configuração

O arquivo `config/constants.py` contém constantes que governarão a execução dos algoritmos. As opções são as seguintes:
 
  - `NUM_ATTRS` (inteiro, default 0) 
   - O número de atributos no conjunto de dados, ou seja, o número de colunas no arquivo csv.
  - `NUM_TARGETS` (inteiro, default 1) 
   - O número de variáveis objetivo, ou seja, o número de colunas no arquivo csv após as colunas de variáveis. 
  - `NORMALIZE_TARGETS` (boolean, default False)
   - Variável que define se as variáveis objetivo também serão normalizadas.
  - `TRAIN_RATIO` (float, default (2.0/3.0) )
   - A proporção dos dados do conjunto original que será usada para compor o conjunto de treinamento. 
  - `INPUT_DELIMITER` (char default ',')
   - O delimitador a ser usado no carregamento do arquivo CSV principal, contendo todos os dados.
  - `HAS_HEADER` (boolean default False)
   - Determina se o CSV principal dos dados possui uma linha de cabeçalho, geralmente usado para definir o nome de cada coluna, que representa um atributo no conjunto de dados ou uma variável objetivo.
  - `NUM_DIGITS` (inteiro)
   - Define o número de algarismos significativos a serem usados na maioria das contas dos algoritmos.
  - `NUM_NEIGHBOURS` (inteiro default 5)
   - Define o número de vizinhos a ser usado no algoritmo KNN.
  - `EXCLUDE_ATTRS` (lista default [])
   - Define os índices (começando em zero) das colunas dos atributos que devem ser ignorados na execução dos algoritmos.
  - `PREDICT_TARGET` (inteiro)
   - Define o índice da coluna que representa a variável objetivo a ser estimada. 
  - `NUM_NEURONS_HIDDEN_LAYER` (inteiro)
   - Número de neurônios a ser usado na (única) camada escondida no algoritmo ANN (rede neural).
  - `LEARNING_RATE` (float default 0.3)
   - Taxa de aprendizado a ser usada no algoritmo ANN (rede neural).
  - `NUM_EPOCHS` (inteiro)
   - Número de épocas (rodadas de treinamento) a serem usadas no algoritmo ANN (rede neural).

### Scripts Principais

Os seguintes scripts são suficientes para mostrar o funcionamento dos algoritmos e devem ser chamados através do interpretador python.

Vale lembrar que todos estes algoritmos usam as configurações definidas no passo anterior.

  - `preprocess_data.py` `<arquivo_csv>`
   - Este script embaralha, normaliza e divide um arquivo csv único em dois arquivos csv: um de teste e um de treinamento.


  - `apply_knn.py` `<diretório_das_partições>`
   - Forneça para este script como argumento o caminho para o diretório contendo as partições (ou seja, um arquivo chamado `train_set.csv` e um chamado `test_set.csv`) de um conjunto de dados. Este script aplicará o algoritmo KNN e escreverá os resultados em um arquivo chamado `prediction_set.csv`, dentro da pasta `predictions_knn/`, no mesmo nível do diretório passado como argumento. 	

  - `train_ann.py` `<diretório_das_partições>`
   - Este script irá, usando o diretório passado como argumento e procurando nele um arquivo chamado `train_set.csv`, treinar uma rede neural com uma camada escondida que sirva para estimar instâncias. Para fins de verificação, o valor final dos pesos bem como a configuração usada para obtê-los (número de épocas, taxa de aprendizado e número de neurônios usados) será escrito na pasta `predictions_ann/`.

  - `train_and_apply_ann.py` `<diretório_das_partições>`
   - Este script executará todos os passos do script anterior e, além disso, aplicará o algoritmo e escreverá os resultados em um arquivo chamado `prediction_set.csv`, dentro da pasta `predictions_ann/`. 

  - `do_metrics.py` `<arquivo_csv_1>` `<arquivo_csv_2>` `<índice>`
   - Este script pode ser usado para calcular o erro médio levando-se em consideração dois conjuntos de dados (em geral um conjunto de teste e o conjunto derivado com as estimativas obtidas por meio de algum algoritmo) e um índice da coluna (começando em zero) que representa o atributo ou variável objetivo cujo erro deseja-se verificar.
