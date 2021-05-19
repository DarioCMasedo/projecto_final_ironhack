import pandas as pd
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

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

# 442
def alineacion_442(valor_total,edad):
    try:
        valor_jugador = valor_total/11
        porteros = goalkeeper(1,valor_jugador,edad).reset_index()
        defensas = defenders(4,valor_jugador,edad).reset_index()
        medios = midfielders(4,valor_jugador,edad).reset_index()
        delanteros = forwards(2,valor_jugador,edad).reset_index()
        pitch = Pitch(pitch_color='grass', line_color='white',stripe=True)
        fig, ax = pitch.draw(figsize=(20, 20))
        annotation = ax.annotate(porteros['short_name'][0], (5, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][0], (24, 30), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][1], (24, 52), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][2], (32, 12), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][3], (32, 68), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][0], (60, 30), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][1], (60, 52), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][2], (60, 12), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][3], (60, 68), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][0], (89, 24), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][1], (89, 60), fontsize=40, ha='center')
        plt.savefig('output/images/442.jpg')
        result = pd.concat([porteros,defensas,medios,delanteros]).reset_index()
        result = result[['short_name','nationality','position', 'age','wage_eur','value_eur','value_pred']]
        return result
    except:
        plt.savefig('output/images/442.jpg')
        return "No se han encontrado jugadores con esos parametros"

# 433
def alineacion_433(valor_total,edad):
    try:
        valor_jugador = valor_total/11
        porteros = goalkeeper(1,valor_jugador,edad).reset_index()
        defensas = defenders(4,valor_jugador,edad).reset_index()
        medios = midfielders(3,valor_jugador,edad).reset_index()
        delanteros = forwards(3,valor_jugador,edad).reset_index()
        pitch = Pitch(pitch_color='grass', line_color='white',stripe=True)
        fig, ax = pitch.draw(figsize=(20, 20))
        annotation = ax.annotate(porteros['short_name'][0], (5, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][0], (24, 30), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][1], (24, 52), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][2], (32, 12), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][3], (32, 68), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][0], (60, 12), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][1], (60, 40), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][2], (60, 68), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][0], (89, 68), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][1], (89, 12), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][2], (89, 40), fontsize=40, ha='center')
        plt.savefig('output/images/433.jpg')
        result = pd.concat([porteros,defensas,medios,delanteros]).reset_index()
        result = result[['short_name','nationality','position', 'age','wage_eur','value_eur','value_pred']]
        return result
    except:
        plt.savefig('output/images/433.jpg')
        return "No se han encontrado jugadores con esos parametros"

# 343
def alineacion_343(valor_total,edad):
    try: 
        valor_jugador = valor_total/11
        porteros = goalkeeper(1,valor_jugador,edad).reset_index()
        defensas = defenders(3,valor_jugador,edad).reset_index()
        medios = midfielders(4,valor_jugador,edad).reset_index()
        delanteros = forwards(3,valor_jugador,edad).reset_index()
        pitch = Pitch(pitch_color='grass', line_color='white',stripe=True)
        fig, ax = pitch.draw(figsize=(20, 20))
        annotation = ax.annotate(porteros['short_name'][0], (5, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][0], (32, 68), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][1], (24, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][2], (32, 12), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][0], (60, 68), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][1], (60, 30), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][2], (60, 52), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][3], (60, 12), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][0], (89, 68), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][1], (89, 12), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][2], (89, 40), fontsize=40, ha='center')
        plt.savefig('output/images/343.jpg')
        result = pd.concat([porteros,defensas,medios,delanteros]).reset_index()
        result = result[['short_name','nationality','position', 'age','wage_eur','value_eur','value_pred']]
        return result
    except:
        plt.savefig('output/images/343.jpg')
        return "No se han encontrado jugadores con esos parametros"
# 532

def alineacion_532(valor_total,edad):
    try:
        valor_jugador = valor_total/11
        porteros = goalkeeper(1,valor_jugador,edad).reset_index()
        defensas = defenders(5,valor_jugador,edad).reset_index()
        medios = midfielders(3,valor_jugador,edad).reset_index()
        delanteros = forwards(2,valor_jugador,edad).reset_index()
        pitch = Pitch(pitch_color='grass', line_color='white',stripe=True)
        fig, ax = pitch.draw(figsize=(20, 20))
        annotation = ax.annotate(porteros['short_name'][0], (5, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][0], (24, 25), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][1], (24, 40), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][2], (35, 8), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][3], (35, 72), fontsize=40, ha='center')
        annotation = ax.annotate(defensas['short_name'][4], (24, 60), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][0], (60, 40), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][1], (60, 12), fontsize=40, ha='center')
        annotation = ax.annotate(medios['short_name'][2], (60, 68), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][0], (89, 24), fontsize=40, ha='center')
        annotation = ax.annotate(delanteros['short_name'][1], (89, 60), fontsize=40, ha='center')
        plt.savefig('output/images/532.jpg')
        result = pd.concat([porteros,defensas,medios,delanteros]).reset_index()
        result = result[['short_name','nationality','position', 'age','wage_eur','value_eur','value_pred']]
        return result
    except:
        plt.savefig('output/images/532.jpg')
        return "No se han encontrado jugadores con esos parametros"