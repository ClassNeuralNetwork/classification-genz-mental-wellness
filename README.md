# 🧠 Gen Z Mental Wellness Analysis using DNN

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto utiliza Redes Neurais Profundas (**DNN**) para classificar e analisar padrões de bem-estar mental e risco de burnout na Geração Z, correlacionando hábitos digitais com indicadores psicológicos.

## 📋 Visão Geral
O objetivo principal é identificar como variáveis de estilo de vida digital (horas de tela, frequência de uso de redes sociais, jogos online) impactam a saúde mental (ansiedade, estresse, qualidade de sono). O modelo utiliza uma arquitetura **MLP (Multilayer Perceptron)** implementada em TensorFlow/Keras.

## 📊 Dataset
O dataset utilizado foi extraído do Kaggle ([Gen Z Mental Wellness Patterns](https://www.kaggle.com/datasets/hammadansari7/gen-z-mental-wellness-and-digital-lifestyle-patterns)). 
- **Atributos:** 22 colunas (Age, Gender, Screen_Time, Social_Media_Usage, Sleep_Hours, etc.)
- **Público-alvo:** Geração Z.
- **Target:** `Burnout_Risk`.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python
- **Bibliotecas Base:** Pandas, NumPy, Scikit-learn
- **IA/ML:** TensorFlow, Keras
- **Visualização:** Matplotlib, Seaborn, Plotly

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Clone o repositório e instale as dependências:

```bash
git clone https://github.com/SeuUsuario/classification-genz-mental-wellness.git
cd classification-genz-mental-wellness
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
