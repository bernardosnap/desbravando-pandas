# %%
import pandas as pd

# %%
df = pd.read_csv("../data/pedido.csv")
df

# %%

filtro_uf = df['descUF'] == "São Paulo"
df[filtro_uf]

# %%

# É de SP e pediu ketchup
filtro_sp_ketchup = (df['descUF'] == "São Paulo") & (df['flKetchup'])
df[filtro_sp_ketchup]

# %%
#Se fosse com o Rio, é do Rio e fez comentário
filtro_rj = (df["descUF"] == "Rio de Janeiro") & (df['txtRecado'])
df[filtro_rj]

# %%
df[filtro_rj].info(memory_usage='deep')



# %%

# Maneira 1
filtro_ufs_ketchup = ((df['descUF'] == "São Paulo") | (df['descUF'] == "Rio de Janeiro") | (df['descUF'] == "Paraná")) & df['flKetchup']
df[filtro_ufs_ketchup]

# %%

# Maneira 2 - mais elegante

ufs = ['São Paulo', "Rio de Janeiro", "Paraná"]
filtro_ufs_ketchup = df['descUF'].isin(ufs) & df["flKetchup"]
df[filtro_ufs_ketchup]

# %%
# Para ver quem nao deixou recado
filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]

# %%
# Para ver quem deixou recado
df[~filtro_txt_na]