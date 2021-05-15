
En este projecto, realizaremos un metodo llamado "Moneyball".

Se trata de encontrar un equipo de futbolistas excepcionales con un presupuesto limitado.

Para comenzar nuestro análisis, necesitábamos un conjunto de datos, sacados de un dataset
de unos 20000 jugadores y con unos 35 atributos para cada jugador.

La idea es construir un equipo de jugadores excepcionales con un presupuesto de 100 millones de euros,
para ello necesitamos entender qué características hacen que un jugador sea excepcional.


    
Lo primero que hago es realizar una limpieza de los datos.

Una vez ya tengamos los datos limpios, teniendo los 35 atributos de cada jugador (variables), realizamos un modelo de prediccion para 
ver el valor de cada jugador, conviertendose esta en nuestra "target".

AL realizar esto, el valor de los jugadores varia mucho segun la posicion del jugador, para ello
separamos en 4 posiciones (porteros,defensas, medios y delanteros).

Una vez ya hecho el primer modelo de prediccion de valor para cada jugador, tenemos que que ver que atributos son los
mejores para cada posicion, llamo a esto, "atributos clave de rendimiento".

Ya teniendo una visualizacion de dichos atributos, selecciono aquellos 5 mejores atributos para cada posicion.

- Porteros:

- Defensas:

- Medios:

- Delanteros: