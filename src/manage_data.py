import pandas as pd

# Dataframe
def carga_data():
    data = pd.read_csv("input/jugadores_20.csv")
    return data


# Desplegable

def lista_personajes():
    data = carga_data()
    return list(data.short_name.unique())