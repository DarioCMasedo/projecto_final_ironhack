
![Prediccion Valor de jugadores de futbol](input/futbol.jpg)

En este projecto, realizaremos machine learning para predecir el valor de los jugadores y luego crear nuestro
propio equipo con un presupuesto y un maximo de edad.


Para comenzar nuestro análisis, necesitamosun conjunto de datos.
Obtengo datos de unos 19 mil jugadores y con unos 35 atributos para cada jugador.

    
Lo primero que hago es realizar una limpieza de los datos.

Una vez ya tengamos los datos limpios, teniendo los 35 atributos de cada jugador (variables), realizamos un modelo de prediccion para 
ver el valor de cada jugador, conviertendose esta en nuestra "target".

Al realizar esto, el valor de los jugadores varia mucho segun la posicion del jugador, para ello
separamos en 4 posiciones (porteros,defensas, medios y delanteros).

Tendremos que ver que atributos son mejores para cada posicion mencionada anteriormente, estos atributos se les puede llamar
"atributos clave de rendimiento".

Ya teniendo una visualizacion de dichos atributos, selecciono los mejores atributos para cada posicion.

- Porteros: 'gk_diving',
 'gk_handling',
 'gk_kicking',
 'gk_reflexes',
 'gk_speed',
 'gk_positioning'.

- Defensas: 'defending_marking',
'defending_standing_tackle',
'defending_sliding_tackle',

- Medios: 'dribbling',
 'skill_fk_accuracy',
 'skill_long_passing',
 'skill_ball_control',
 'mentality_vision',

- Delanteros: 'mentality_positioning',
 'attacking_finishing',
 'movement_reactions',
 'skill_ball_control',
 'power_shot_power',




Ya con los atributos en mano, hacemos ml, un modelo por posicion, utilizando las librerias H20, sklearn
Teniendo el modelo, guardado en notebooks/prediccion_jugadores, es hora de hacerlo en streamlit.


Podremos elegir entre varias alineaciones

- 442
- 433
- 343
- 532

Un presupuesto en millones y un maximo de edad para que nos haga el equipo.



### DISTRIBUCION DEL REPOSITORIO

- Notebooks ---> limpieza de los datos, modelos de machine learning, alineaciones utilizadas en el projecto.
- Input ---> imagen de la portada y datos de los jugadores.
- Output ---> Datos limpios, predicciones por cada posicion, atributos importantes por posicion y alineaciones.
- Src ---> Archivo que contiene las funciones utilizadas
- Streamlit.py ---> Arranca la aplicacion : streamlit run streamlit.py


## LIBRERIAS UTILIZADAS


* [Pandas](https://pandas.pydata.org/)
* [Kaggle](https://www.kaggle.com/)
* [Streamlit](https://streamlit.io/)
* [Plotly](https://plotly.com/python/)
* [MLP-Soccer](https://pypi.org/project/mplsoccer/)
* [Jupyter](https://jupyter.org/)
* [Python](https://www.python.org/)
* [Sklearn](https://scikit-learn.org/stable/)
* [H2O ai](https://www.h2o.ai/)
