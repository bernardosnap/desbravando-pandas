# %%
import pandas as pd

# %%

# Isso é uma lista!!!!
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]

# %%
s_idade = pd.Series(idade)
s_idade

# %%

# Métodos das Séries
media = s_idade.mean() #média
variancia = s_idade.var() #variância
des_pad = s_idade.std() #desvio padrão
describe = s_idade.describe() #estatistica descritiva
describe

# %%

nova_idade=[]
for i in idade:
    if i >= 30:
        nova_idade.append(i)

nova_idade #fazer for não é performático

# %%

filtro = s_idade >= 30 #o filtro são os elementos maiores ou iguais a 30
s_idade[filtro] #mostra na série os elementos maiores ou iguais a 30
# s_idade[~filtro] #mostra na série os elementos menores que 30

# %%

filtro = [True, False, True, True, False, False, False, False, True]
s_idade[filtro]
