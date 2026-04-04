# -*- coding: utf-8 -*-
"""Projeto/Artigo Unidade 1

Código iniciado em aula - Análise de Saúde Mental Gen Z
"""

# Importa o NumPy para manipulação de arrays e cálculos matemáticos
import numpy as np 

# Importa o Pandas para carregar e manipular tabelas de dados (DataFrames)
import pandas as pd 

# Importa o Pyplot do Matplotlib para criação de gráficos básicos
import matplotlib.pyplot as plt 

# Importa o TensorFlow, framework principal para criação da rede neural
import tensorflow as tf 

# Ferramenta para dividir os dados em conjuntos de Treino e Teste
from sklearn.model_selection import train_test_split 

# Ferramenta para normalizar os dados (deixar todos na mesma escala numérica)
from sklearn.preprocessing import StandardScaler 

# Métricas para avaliar modelos de regressão (Erro Médio Quadrático e R2)
from sklearn.metrics import mean_squared_error, r2_score 

# Importa o Seaborn para criar gráficos estatísticos mais bonitos e fáceis
import seaborn as sns 

# Importa o Plotly Express para criar gráficos interativos (web)
import plotly.express as px 

# Ferramenta para transformar colunas de texto em várias colunas de 0 e 1 (binário)
from sklearn.preprocessing import OneHotEncoder 

# Ferramenta para transformar textos de categorias em números sequenciais (0, 1, 2...)
from sklearn.preprocessing import LabelEncoder 

# Carrega o arquivo CSV. O 'sep' indica que as colunas são separadas por vírgula.
dados = pd.read_csv('data/genz_mental_wellness_synthetic_dataset.csv', sep=',')

# Exibe as 10 primeiras linhas da tabela para conferência inicial
dados.head(10)

# Exibe a dimensão dos dados (Quantas linhas e quantas colunas existem)
dados.shape

# Exibe informações técnicas: nomes das colunas, tipos de dados e se há valores nulos
dados.info()

# Configura o estilo visual dos gráficos do Seaborn para ter uma grade branca ao fundo
sns.set_style('whitegrid')

# Define a paleta de cores 'deep' para os gráficos
sns.set_palette('deep')

# Cria um gráfico de barras contando quantos registros existem para cada 'País' (Country)
sns.countplot(x=dados['Country'])

# Comando para renderizar e mostrar o gráfico na tela
plt.show()