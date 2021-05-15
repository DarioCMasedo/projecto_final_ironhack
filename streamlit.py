import streamlit as st
from PIL import Image
from streamlit import uploaded_file_manager
from streamlit.logger import update_formatter
import src.manage_data as data
import plotly.express as px
import pandas as pd
import folium
#from streamlit import folium_static
import codecs
import streamlit.components.v1 as components


st.write("""
hola mundo
""")

# Cargar dataframe 

 # dataframe = carga_data()

# st.dataframe(data.carga_data())



# Jugadores
personaje = st.selectbox(

    "Selecciona un jugador", data.lista_personajes()
)