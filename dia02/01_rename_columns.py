# %%
import pandas as pd

# %%
df = pd.read_csv("../data/pedido.csv")
df

# %%
## Maneira 1 - está retornando um dataframe novo, por isso temos que nomear
## É O CASO MAIS UTILIZADO
df = df.rename(columns={"descUF": "descEstado"})
df.sample(10)

# %%
# Maneira 2 - está alterando o próprio dataframe
df.rename(columns={"descUF": "descEstado"}, inplace=True)