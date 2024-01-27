# %%
import pandas as pd

# %%

data = {
    "nome":["Téo", "Nah", "Maria", "José", "Marina", "Jessica", "InfoSlack"],
    "idade":[30, 33, 2, 45, 65, 43, 40],
    "cor": ["Preto", "Verde", "Azul", "Vermelho", "Amarelo", "Verde", "Azul"],
    "renda": [3566, 1345, 0, 6576, 4325, 5326, 10244],
    "signo": ['Virgem', 'Peixes', 'Sagitário', 'Peixes','Virgem', 'Peixes', 'Leão']
}

data["idade"]

# %%
df = pd.DataFrame(data)
df['idade']

# %%
type(df["idade"]) #mostra que é uma série

# %%

df[['idade', 'renda']].describe()
df[['idade', 'renda']].mean()

# %%

df.info(memory_usage='deep')