# criptwit
## En qué consiste.
En este proyecto he investigado sobre la ingfluencia de los twits de Elon Musk en el precio de las principales criptomonedas cuando hace mencion de estas en sus twits.
## Citación de fuentes
Lo que hemos hecho ha sido utilizar la base de datos https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021 que recopial todos los twits del multimillonario desde 2010 hasta 2021.

## Código requerido
Para poder medir el impacto de sus twtis hemos hecho uso de la API https://www.coingecko.com/ y el wrapper https://github.com/man-c/pycoingecko

Se ha desarrollado en lenguaje python y hemos requerido de las siguientes librerías:

. sys
· pandas
· re
· time
· pycoingecko
· matplotlib.pyplot

## Descripción
El código principal corre desde criptiwt.py y hace diferentes llamadas a las librerías propias siguientes:

· lib_ini: para la inicialización del programa.
· lib_cleaner: para la limpieza del DF.
· lib_curren: para la gestiones de las criptomonedas y consulta a la API.
· lib_calc: para la elaboración de cálculos
· lib_visual: para el ploteo y almacenado de imágenes.

El código descargará automáticamente la BD de kaggle y la descomprimirá con ZIP (requerido) en la carpeta 'data'. 

Es necesario indicarle las monedas a investigar mediante el archivo de texto currencies_list_symbol_name.txt que debe estar en la carpeta 'src' y debe contener el símbolo de las monedas en la líneas impares y su nombre en la siguiente.
## Salidas
El programa nos guardará en la carpeta 'output' tanto las cirvas del precio como la gráfica de barras.

### Evolucíon del precio por twits
En la gráfica del precio se superpone el precio de la moneda de las 72h antes al twit correspondiente con las 72 h posteriores diferenciadas por colorres. La referencia para ambas gráficas se ha referenciado al precio de la moneda en el instante del twit

### Gráfica de barras
En cada gráfica vemos el porcentaje de tiempo de las 72h anteriores en las que el precio de la moneda  ha estado por debajo del precio en las 72h posteriores.
