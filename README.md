
(input/futbol.jpg.jpg)

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

- Porteros:

- Defensas:

- Medios:

- Delanteros:

Ya con los atributos en mano, hacemos ml, un modelo por posicion, utilizamos las librerias H20, sklearn.....




## LIBRERIAS UTILIZADAS

* [Streamlit](https://streamlit.io/)
* [MLP-Soccer](https://pypi.org/project/mplsoccer/)
* [Jupyter](https://jupyter.org/)
* [Python](https://www.python.org/)
* [Sklearn](https://scikit-learn.org/stable/)
* [H2O ai](https://www.h2o.ai/)
