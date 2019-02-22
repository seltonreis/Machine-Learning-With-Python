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

