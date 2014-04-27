ml201401
========

### Instructions (Portuguese)

  - Baixar este projeto ( através do git é só dar git clone ou então também pode baixar o .zip do projeto)
  - os dados já estão nos lugares corretos - (data/(nome_do_projeto)/original_data)
  - mexa no arquivo config/constants.py para configurar o algoritmo com as informações do seu conjunto de dados (tem as sugestões de configuração no arquivo README dentro da pasta de cada conjunto de dados)
  - rode o script preprocess_data.py com o python.
   
   - Exemplo: python preprocess_data.py data/concrete/original_data/Concrete_Data.csv
   
  - O passo anterior deve ter criado dois arquivos no diretório data/(nome_do_projeto)/partitions. Um com o nome train_set.csv e outro com o nome test_set.csv
  - Agora rode o script apply_knn.py com o python, passando como parâmetro o caminho para a pasta onde estão as partições (aquele criado no passo anterior)
   
   - Exemplo: python apply_knn.py data/concrete/partitions

  - O passo anterior deve ter criado um arquivo chamado prediction_set.csv, dentro da pasta data/(nome_do_projeto)/predictions. Este arquivo contém as previsões calculadas pelo algoritmo. 

 
### Description

 Little ML (Machine Learning) toolkit with utilities and some data for testing as well.
 
 This includes some helpers to manipulate files, clean data and so on.
 
###TODO
  - Unit test functions using sample files.

**P.S.:** This is a WIP (work in progress). Keep in mind that I had no prior Python experience before doing this. One of the aims of this project is precisely to get me some Python experience.
