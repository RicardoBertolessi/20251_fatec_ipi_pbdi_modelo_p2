#REQ 1
# faça os imports que julgar necessários
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#REQ 2
#essa função deve devolver a base de dados
def ler_base():
  dataset = pd.read_csv(r'dados.csv')
  print(dataset)
  return dataset

df = ler_base()
#REQ 3
#essa função recebe a base lida anteriormente
#ela deve devolver uma tupla contendo as features e a classe
def dividir_em_features_e_classe(dataset):
  features = dataset.iloc[:, :-1].values
  classe = dataset.iloc[:, -1].values
  return features, classe

base = ler_base()
features, classe = dividir_em_features_e_classe(base)
#REQ 4
#essa função recebe as features
#ela deve devolver as features da seguinte forma
#Valores faltantes da coluna "Gastos com pesquisa e desenvolvimento": substituir pela média
#Valores faltantes da coluna "Gastos com administracao": substituir pela mediana
#Valores faltantes da coluna "Gastos com marketing": Substituir por zero
#Valores faltantes da coluna "Estado": Substituir pela moda
def lidar_com_valores_faltantes(features):
  imputer_media = SimpleImputer(missing_values=np.nan, strategy="mean")
  features[:, [0]] = imputer_media.fit_transform(features[:, [0]])

  imputer_mediana = SimpleImputer(missing_values=np.nan, strategy="median")
  features[:, [1]] = imputer_mediana.fit_transform(features[:, [1]])

  imputer_zero = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0)
  features[:, [2]] = imputer_zero.fit_transform(features[:, [2]])

  imputer_moda = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
  features[:, [3]] = imputer_moda.fit_transform(features[:, [3]])
  return features

features, classe = dividir_em_features_e_classe(base)
features_tratadas = lidar_com_valores_faltantes(features)

#REQ 5
#essa função recebe as features
#ela deve devolver as features da seguinte forma
#Variável "Estado": Codificar com OneHotEncoding
def codificar_categoricas(features):
  columnTransformer = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [3])],
    remainder='passthrough' 
    )
  features = columnTransformer.fit_transform(features)
  return features
features = codificar_categoricas(features)

#REQ 6
#essa função recebe as features e a classe
#ela deve devolver uma tupla com 4 itens
# features de treinamento, features de teste, classe de treinamento, classe de teste
# a base de treinamento deve ter 75% das instâncias
def obter_bases_de_treinamento_e_teste(features, classe):
  pass

#REQ 7
#essa função recebe as features de treinamento e de teste
#ela deve devolver uma tupla com 2 itens, da seguinte forma
#todas as variáveis normalizadas com o método MinMax
def normalizar(features_treinamento, features_teste):
  pass

#REQ 8
def vai():
  #chame as suas funções aqui
  #exiba as quatro bases aqui
     pass

vai()