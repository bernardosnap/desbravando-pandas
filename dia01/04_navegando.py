# %%
import pandas as pd

df = pd.read_csv("../data/pedido.csv")
df

# %%

# SELECT idPedido, flKetchup from pedido
df[['idPedido', 'flKetchup']]

# %%

# SELECT idPedido, descUF, flKetchup, txtRecado, dtPedido
# from pedido

colunas = [
    'idPedido',
    'descUF',
    'flKetchup',
    'txtRecado',
    'dtPedido',
]

df = df[colunas]

# %%
# Maneira de colocar as colunas em ordem alfabética
ordem_alfabetica = df.columns.tolist()
ordem_alfabetica.sort()
df[ordem_alfabetica]

# %%
# Cria um dataframe novo com 100 dados aleatórios do antigo
df_sample = df.sample(100)

# %%
df_sample.iloc[0]

# %%
df.loc[33:384]

df.loc[[33,384]]

# %%
df_sample.iloc[0:10][['idPedido', 'dtPedido']]

# %%
rio = df_sample["descUF"] == "Rio de Janeiro"
df_sample[rio][['idPedido','dtPedido','txtRecado']]
# rio[['idPedido','dtPedido','txtRecado']]

# o iloc pega o elemento que está na posiçao, por exemplo, iloc[5] pega o elemento na posicao 5 do dataframe
# o loc pega o elemento que tem o indice, por exemplo, loc[5] pega o elemento que tem indice 5 no dataframe