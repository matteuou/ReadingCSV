# 🚀 Guia de Análise de Dados com Pandas: Importação e Exploração Inicial
Este projeto documenta as etapas essenciais para iniciar um fluxo de trabalho de análise de dados utilizando a biblioteca Pandas em Python, focando na importação, inspeção e identificação da estrutura de conjuntos de dados.

# 🛠️ Tecnologias e Dependências
As seguintes tecnologias foram utilizadas e são necessárias para replicar o ambiente:

Python 3.x

Pandas (Instalação: pip install pandas)

(Opcional) Jupyter Notebook ou outro ambiente de desenvolvimento interativo.

# 📁 Conjuntos de Dados Utilizados
O projeto utiliza dois arquivos no formato CSV como fonte de dados:

Airplane.csv

modelos.csv

# 📥 1. Importação de Dados
A importação dos arquivos CSV para a memória foi realizada utilizando a função pd.read_csv(), que converte os dados em DataFrames da Pandas.

Código de Importação:

Python

import pandas as pd

# Importação dos DataFrames com delimitador ',' e encoding 'utf-8'
df_aviao = pd.read_csv("Airplane.csv", sep=",", encoding="utf-8")
df_modelos = pd.read_csv("modelos.csv", sep=",", encoding="utf-8")


# 🔍 2. Inspeção Inicial dos Dados (.head())
A inspeção inicial é crucial para validar a importação, confirmar o formato dos dados e identificar anomalias nas primeiras linhas.

Método Aplicado:

O método .head() foi usado para visualizar as 5 primeiras linhas de cada DataFrame.



# Visualiza as 5 primeiras linhas de df_aviao
df_aviao.head()

# Visualiza as 5 primeiras linhas de df_modelos
df_modelos.head()


✅ Carga Correta: Confirma que o arquivo foi lido sem erros.

✅ Delimitadores e Encoding: Verifica se as colunas estão separadas corretamente e se caracteres especiais foram decodificados.

✅ Tipos Básicos: Permite uma primeira observação dos tipos de dados nas colunas.

# 🧱 3. Identificação da Estrutura e Colunas
O conhecimento exato dos nomes das colunas e da estrutura geral dos DataFrames é fundamental para o planejamento das próximas fases de tratamento.

Método Aplicado:

O atributo .columns de cada DataFrame foi inspecionado para listar todos os nomes das colunas.



# Lista as colunas do DataFrame 'df_aviao'
df_aviao.columns

# Lista as colunas do DataFrame 'df_modelos'
df_modelos.columns
Benefícios:

# Mapeamento: Cria um mapa mental da estrutura do dado.

Colunas-Chave: Ajuda a identificar colunas que podem ser usadas para futuras integrações (merge) entre os DataFrames.

Planejamento de Limpeza: Aponta a necessidade de renomear ou padronizar nomes de colunas.

