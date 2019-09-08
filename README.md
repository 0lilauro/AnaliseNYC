# Análise de dados NYC Taxi Trips 

**Autor:** Lauro César de Oliveira Teixeira

**Data:** Belo Horizonte - 12 de Agosto de 2019 

**Versão:** 1.0

**Contato:** [Github](https://github.com/0lilauro) - [LinkedIn](https://www.linkedin.com/in/laurocoliveira) - [Gmail](0lilauro@gmail.com)

## Introdução

> Este trabalho tem como o objetivo fazer uma análise em cima de uma base dados sobre as viagens de táxi em Nova York no ano de 2009 a 2012. Todos os dados usados foram disponibilizados pela Data Sprints e estão sendo armazenados em buckets da Amazon para uma melhor disponibilidade, mas originalmente são derivados de fontes de dados abertas. Bases semelhantes podem ser encontradas no [Keggle](https://www.kaggle.com/) ou em sites como [NYC.gov](https://www1.nyc.gov/site/tlc/index.page), um site governamental que disponibiliza algumas DGA’s (Dados Governamentais Abertas).
>
> O intuito dessa análise é mostrar de forma bem simples a manipulação de bases de dados muito grandes, utilizando serviços da amazon para melhor processamento e linguagens como SQL e Python para consultar, manipular e criar visualizações gráficas de forma eficiente e simples.
>
> As tecnologias usadas para a composição desta análise são:  
> - [Notebooke Jupyter](https://jupyter.org/)
> - [Python 3.6](https://www.python.org/)
> 
> E as bibliotecas utilizadas foram:
> - [Vega](https://github.com/vega/ipyvega)
> - [Altair](https://altair-viz.github.io/index.html)
> - [Matplotlib](https://matplotlib.org/)
> - [Numpy](https://www.numpy.org/)
> - [Pandas](https://pandas.pydata.org/)
> - [Postgres Connector (Psycopg2)](https://pypi.org/project/psycopg2/)
>
> Ao decorrer da análise, todas as bibliotecas utilizadas serão explicadas com mais detalhes para que o leitor não sinta-se prejudicado por não entender o porque e como está sendo a implementação de cada parte do código.
>
> Todo a análise foi estruturada utilizando Notebook Jupyter utilizando conexões públicas com o banco de dados da Amazon Redshift, e pode ser encontrada no 
[nbviewer](). Além de estar disponivel no arqui Analise.html do diretório atual.
>
> Só é necessária a lida do arquivo para entender todo o estudo.
>
> Referências externas como o código que faz o ETL das viagens, foram executados em uma máquina EC2 da Amazon, mas seu script está disponibilizado aqui como *prod_etl_trip.py*. Ele utiliza a uma conta de usuário diferente para ter acesso a comandos de insert, delete e update no banco de dados, por isso,
não foi disponibilizada aqui.
>
> Para a execução do script citado anteriormente, baixe o repositório e tenha o python3(3.6) e pip3 instaladas na máquina. Após fazer isso, utilize os seguintes comandos: 
```sh
$ pip install -r requirements.txt
```
>
> Agora só basta ajustar as variáveis de conexão da função **get_connection** e executar o seguinte script: 
```sh
$ python3 prod_etl_trip.py
```
>
> Caso haja interesse em fazer conexões para testar a base de dados da Amazon Redshift, a conexão com permissões para selecionar, estará disponível nos próximos 15 dias. Suas credenciais são:
>
>
> * **host**: redshift-cluster-nyc.cyy2ldnhnbji.us-east-2.redshift.amazonaws.com
> * **user**: analytics
> * **database**: analyze
> * **port**: 5439	
> * **password**: wVRF2iWdqoEHX3EeFLwugh
