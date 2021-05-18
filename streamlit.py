import streamlit as st
from PIL import Image
from streamlit import uploaded_file_manager
from streamlit.logger import update_formatter
import src.funciones as fun
import plotly.express as px
import pandas as pd
import folium
#from streamlit import folium_static
import codecs
import streamlit.components.v1 as components
from mplsoccer.pitch import Pitch



porteros = pd.read_csv('output/predict_posiciones/porteros.csv')
defensas = pd.read_csv('output/predict_posiciones/defensas.csv')
medios = pd.read_csv('output/predict_posiciones/medios.csv')
delanteros = pd.read_csv('output/predict_posiciones/delanteros.csv')


st.write("""

    Monta tu equipo

""")


n = st.selectbox(

    "Selecciona una alineacion", ["442","433","343","532"]

)


#

_input = st.text_input("Introduce tu presupuesto en millones de €")
_input2 = st.text_input("Introduce edad maxima de los jugadores")

if _input and _input2 and n == "442":
    ax = fun.alineacion_442(int(_input),int(_input2))
    image = Image.open('output/images/442.jpg')
    st.write(ax)
    st.image(image)
elif _input and _input2 and n == "433":
    ax = fun.alineacion_433(int(_input),int(_input2))
    image = Image.open('output/images/433.jpg')
    st.write(ax)
    st.image(image)
elif _input and _input2 and n == "343":
    ax = fun.alineacion_343(int(_input),int(_input2))
    image = Image.open('output/images/343.jpg')
    st.write(ax)
    st.image(image)
elif _input and _input2 and n == "532":
    ax = fun.alineacion_532(int(_input),int(_input2))
    image = Image.open('output/images/532.jpg')
    st.write(ax)
    st.image(image)
else:
    st.write('No hay datos seleccionados')