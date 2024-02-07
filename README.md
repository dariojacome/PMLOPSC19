<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

 <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
 **Presentado por:** Oscar Darío Jácome Prado
 **Correo:** dariojp94@gmail.com
 <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

</div>
<h1 align="center">  Descripción </h1>
Este repositorio alberga mi primer proyecto individual durante la etapa de Labs en Henry, donde desempeño el rol de MLOps Engineer. El proyecto se centra en la transición de un modelo de recomendación al entorno real, abarcando la preparación de datos.

<h1 align="center">  Contexto y Rol </h1>

Como Data Scientist en Steam, me encuentro con el desafío de predecir el precio de los videojuegos. La tarea se complica debido a la presencia de numerosos datos nulos en diversas columnas y la existencia de información que podría no ser relevante para mi modelo. Para abordar eficazmente este desafío, asumiré tanto el rol de Data Engineer como el de MLOps Engineer.


<h1 align="center">  Propuesta de trabajo  </h1>

En primer lugar, se llevó a cabo una adecuación de las bases de datos mencionadas. A través de tres cuadernos, se procedió a eliminar duplicados, valores nulos y columnas que no serían utilizadas. Luego, se establecieron relaciones entre estas tres bases de datos con el fin de obtener un Producto Mínimo Viable (MVP).

Para facilitar la manipulación de datos, se extrajeron las tres bases de datos y se las gestionó de manera más eficiente en el cuaderno [apis.ipynb](https://github.com/dariojacome/PMLOPSC19/blob/main/apis.ipynb). Posteriormente, para compartir estos datos en GitHub, se convirtieron en archivos .parquet.

Una vez completado este proceso, se importaron los datos en el cuaderno [apis.ipynb](https://github.com/dariojacome/PMLOPSC19/blob/main/apis.ipynb) y se crearon funciones para realizar diversas consultas conforme a los requisitos del proyecto.
<h2 align="center">  Desarrollo API </h2>

Se crea una API para realizar consultas sobre los datos:

- Consulta de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items. ``def userdata( User_id : str )`` 
- Consulta  de cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos en base a reviews.recommend ``def countreviews( YYYY-MM-DD y YYYY-MM-DD : str )`` 
- Consulta el puesto en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.. ``def genre( género : str )`` 
- Consulta de los top 5 juegos de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.``def userforgenre( género : str )``  
- Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.  ``def developer( desarrollador : str )``  
- Consulta  el año y devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.  ``def sentiment_analysis( año : int )``  


## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
+ [Solución de los problemas planteados](https://github.com/dariojacome/PMLOPSC19/blob/main/apis.ipynb): Cuaderno de jupyter donde está solucionado las funciones pedidas
+ [Limpieza DB juegos](https://github.com/dariojacome/PMLOPSC19/blob/main/game.ipynb): cuaderno que indica como se hizo la limpieza de datos y reordenamiento de la base de datos de los juegos para luego ser usada en apis.ipynb
+ [Limpieza DB usuarios ](https://github.com/dariojacome/PMLOPSC19/blob/main/user_data.ipynb): cuaderno que indica como se hizo la limpieza de datos y reordenamiento de la base de datos de los usuarios para luego ser usada en apis.ipynb
+ [Limpieza DB reviews ](https://github.com/dariojacome/PMLOPSC19/blob/main/reviews.ipynb): cuaderno que indica como se hizo la limpieza de datos y reordenamiento de la base de datos de las opiniones de los usuarios para luego ser usada en apis.ipynb
