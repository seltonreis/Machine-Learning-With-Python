"""
Created on Thu Feb 21 20:14:08 2019

@author: selton
"""

import pandas as pd #importa biblioteca pandas e transforma em pd
base = pd.read_csv('credit_data.csv') #faz a leitura da base de dados credit_data.csv
base.describe() #faz a descrição da base de dados
base.loc[base['age'] < 0] #localiza valores negativos da idade para possiveis correções
#apagar toda coluna 'age'
base.drop('age', 1, inplace=True)
#apagar somente os registros com problema
base.drop(base[base < 0].index, inplace=True)
#preencher os valores manualmente
#preencher os valores com a média (mais indicado)
base.mean() #média de todas as colunas
base['age'].maen() #média somente da coluna 'age' obs: c dados invalidos
base['age'][base.age > 0].mean() #média somente dos valores acima de 0.
base.loc[base.age < 0, 'age'] = 40.92 #substitui os valores negativos das idades pelas médias.

pd.isnull(base['age']) #procura os valores em branco da coluna 'age'
base.loc[pd.isnull(base['age'])] #localiza somente as linhas com valores nulos em 'age'

previsores = base.iloc[:, 1:4].values #cria uma variável com tods as linhas e com as colunas 1 a 3.
classe = base.iloc[:, 4].values #cria uma variável com todas as linhas e com a coluna 4.

from sklearn.preprocessing importer Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis = 0) #seleciona apenas valores 'NaN' e substitui pela média
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])
