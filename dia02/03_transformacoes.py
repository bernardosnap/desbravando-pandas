# %%

import pandas as pd
import numpy as np

# %%

df = pd.read_csv("../data/produto.csv")
df

# %%

df["precoAjustado"] = (df["vlPreco"] * 1.09).round(2)
df

# %%

df["txAjuste(%)"] = (100 *( df["precoAjustado"] / df["vlPreco"] - 1)).round(2)
df

# %%
df["taCaro"] = df["precoAjustado"] >= 10
df

# %%
# Para aplicar um logaritmo
df["logTxAjuste"] = np.log(df['txAjuste(%)'])

# %%
# Para aplicar uma exponencial
df["expTxAjuste"] = np.exp(df['txAjuste(%)'])
df

# %%
#Para retirar uma coluna
df = df.drop(columns=["expTxAjuste"])
df


# %%
#Função para calcular o fatorial
def teozinho(x):
    total = 1
    for i in range(2,int(x)+1):
        # total = total * i
        total *= i
    return total

# %%
#o apply serve para aplicar uma função aos dados
df["fatorialPreco"] = df["precoAjustado"].apply( teozinho )
df