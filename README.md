📊 Data Import & Exploration with Pandas

Este projeto demonstra as etapas iniciais do fluxo de análise de dados utilizando Python e a biblioteca Pandas, com foco em:

Importação de arquivos .csv

Inspeção preliminar dos dados

Identificação da estrutura e colunas dos DataFrames

O objetivo é estabelecer a base técnica necessária para etapas posteriores como limpeza, transformação e análise.

🛠️ Tecnologias Utilizadas

Python 3.x

Pandas

(Opcional) Jupyter Notebook

Arquivos CSV utilizados:

Airplane.csv

modelos.csv

📥 Importação de Dados

A importação de dados externos foi realizada utilizando o método read_csv():

import pandas as pd

df_aviao = pd.read_csv("Airplane.csv", sep=",", encoding="utf-8")
df_modelos = pd.read_csv("modelos.csv", sep=",", encoding="utf-8")


Esses DataFrames servem como estrutura base para manipulação e análise dos datasets.

🔍 Inspeção Inicial dos Dados (.head())

Para validar a importação e visualizar rapidamente a estrutura das primeiras linhas, foi utilizado o método:

df_aviao.head()
df_modelos.head()


Essa etapa é fundamental para:

Verificar se os dados foram carregados sem erros

Observar possíveis inconsistências iniciais

Confirmar delimitadores, encoding e tipos básicos

🧱 Identificação da Estrutura e Colunas

Foi realizada a inspeção das colunas presentes em cada dataset:

df_aviao.columns
df_modelos.columns


Isso permite:

Mapear a estrutura dos dados

Identificar possíveis colunas-chave

Planejar etapas de limpeza e transformação

Compreender tabelas com múltiplos atributos

📌 Resultados e Conclusão

Após a execução das etapas acima, obteve-se:

Importação correta dos arquivos CSV

Visualização inicial da estrutura dos dados

Identificação clara das colunas de cada DataFrame

Essas operações formam a base do processo de Análise de Dados, permitindo avançar para etapas mais complexas como:

Remoção de inconsistências

Tratamento de valores ausentes

Conversões de tipo

Integração entre tabelas

Análises estatísticas
