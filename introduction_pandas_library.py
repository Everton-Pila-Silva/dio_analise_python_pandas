# -*- coding: utf-8 -*-
"""introduction_pandas_library.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M1AfSUGEN0J71ilbwLZTZ2UA-0ikuC5q

# **Python para Análise de dados (Pandas)** - Everton Pila Silva
"""

# Importando a biblioteca pandas
import pandas as pd

df = pd.read_csv("./datasets/Gapminder.csv", sep=";")

# Visualizando as 5 primeiras linhas
df.head()

df.rename(columns={
            'country': 'Pais',
            'continent': 'Continente',
            'year': 'Ano',
            'lifeExp': 'ExpectativaVida',
            'pop': 'PopulacaoTotal',
            'gdpPercap': 'PIB'
            })

df = df.rename(columns={
            'country': 'Pais',
            'continent': 'Continente',
            'year': 'Ano',
            'lifeExp': 'ExpectativaVida',
            'pop': 'PopulacaoTotal',
            'gdpPercap': 'PIB'
            })

df.head(10)

# Total de linhas e colunas
df.shape

df.columns

df.dtypes

df.tail(10)

# Informações estatísticas do DF
df.describe()

df['Continente'].unique()

oceania = df.loc[df['Continente'] == 'Oceania']
oceania.head(5)

oceania['Pais'].unique()

# Faz a contagem do número de países agrupados por continente
df.groupby("Continente")["Pais"].nunique()

# Expectativa de vida média por ano
df.groupby("Ano")["ExpectativaVida"].mean()

df['PIB'].mean()

df['PIB'].sum()

df.shape[0]

df["PIB"].sum() / df.shape[0]