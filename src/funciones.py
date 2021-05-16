import pandas as pd

porteros = pd.read_csv('output/predict_posiciones/porteros.csv')
defensas = pd.read_csv('output/predict_posiciones/defensas.csv')
medios = pd.read_csv('output/predict_posiciones/medios.csv')
delanteros = pd.read_csv('output/predict_posiciones/delanteros.csv')

def goalkeeper(numero, valor_jugador,edad):
    gk = porteros.loc[(porteros['value_pred'] <= valor_jugador) & (porteros['age'] <= edad)]
    gk.sort_values(by = 'value_pred', inplace = True, ascending = False)
    gk = gk.nlargest(numero, columns="value_pred")
    return gk

def defenders(numero, valor_jugador,edad):
    defend = defensas.loc[(defensas['value_pred'] <= valor_jugador) & (defensas['age'] <= edad)]
    defend.sort_values(by = 'value_pred', inplace = True, ascending = False)
    defend = defend.nlargest(numero, columns="value_pred")
    return defend

def midfielders(numero, valor_jugador,edad):
    mid = medios.loc[(medios['value_pred'] <= valor_jugador) & (medios['age'] <= edad)]
    mid.sort_values(by = 'value_pred', inplace = True, ascending = False)
    mid = mid.nlargest(numero, columns="value_pred")
    return mid

def forwards(numero, valor_jugador,edad):
    forw = delanteros.loc[(delanteros['value_pred'] <= valor_jugador) & (delanteros['age'] <= edad)]
    forw.sort_values(by = 'value_pred', inplace = True, ascending = False)
    forw = forw.nlargest(numero, columns="value_pred")
    return forw


# Alineaciones