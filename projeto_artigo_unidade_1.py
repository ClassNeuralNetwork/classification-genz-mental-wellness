# -*- coding: utf-8 -*-
"""Projeto/Artigo Unidade 1

Código iniciado em aula - Análise de Saúde Mental Gen Z
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import mean_squared_error, r2_score 
import seaborn as sns 
import plotly.express as px 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder 

dados = pd.read_csv('data/genz_mental_wellness_synthetic_dataset.csv', sep=',')
dados.head(10)
dados.shape

dados.info()

sns.set_style('whitegrid')
sns.set_palette('deep')

sns.countplot(x=dados['Country'])

plt.show()