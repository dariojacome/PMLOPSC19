from fastapi import FastAPI
import pandas as pd



# crea instancia de fastapi
app = FastAPI()
app.title = 'Solucion MLOPS Henry'

# crear punto de entrada o endpoint


@app.get('/')
def mensaje():
    return 'Hola, bienvenido a FastAPI '

@app.get('/developer/')
def developer(desarrollador: str) -> dict:
    
    df_dev=pd.read_csv('1punto.csv')

    # Filtrar el DataFrame para obtener solo las filas correspondientes al desarrollador especificado
    df_filtrado = df_dev[df_dev['developer'].str.lower() == desarrollador.lower()]
    


    # Calcular la cantidad de items por año
    cantidad_items_por_anio = df_filtrado.groupby('Año').size()

    # Calcular el porcentaje de contenido gratuito por año
    porcentaje_contenido_gratuito_por_anio = (df_filtrado.groupby('Año').size())/((cantidad_items_por_anio).sum())*100



    return { 'Anio':df_filtrado['Año'].iloc[1:].tolist(),'cantidad': cantidad_items_por_anio.tolist(), 'Contenido Free': porcentaje_contenido_gratuito_por_anio.tolist()
    }



@app.get('/userdata/') 
def userdata(user_id: str) -> dict:
    user_id = user_id.lower()
    df_datauser=pd.read_parquet('2punto.parquet')
    comprobar = list(set(df_datauser['user_id']))
    if user_id in comprobar:
           
         # Filtrar el DataFrame por el usuario especificado
        user_data = df_datauser[df_datauser['user_id'] == user_id]
        
        # Contar las repeticiones del usuario
        contador = user_data.shape[0]
        
        # Sumar la columna 'price' para las filas correspondientes al usuario
        suma_precios = user_data['price'].sum()
        # Filtrar las filas donde la columna 'recommend' es True y luego sumar esos valores para dividirlos entre el contador
        promedio = (user_data[user_data['recommend'] == True]['recommend'].sum())*100/contador


        return {
            'el usuario': user_id, 'gasto en dolares': suma_precios, 'porcentaje de recomendacion': promedio, 'cantidad items': contador
        }
    else:
        return 
    
@app.get('/userforgenre/') 
def UserForGenre( genero : str ):
    
    genero = genero.capitalize()
    #importamos el 3 punto 
    df_genre=pd.read_parquet('3punto.parquet')

    # Encontrar el usuario con más horas jugadas para el género dado
    usuario_mas_horas = df_genre.groupby('user_id')[genero].sum().idxmax()
    

    # Filtrar el DataFrame para el usuario con más horas jugadas
    df_usuario_mas_horas = df_genre[df_genre['user_id'] == usuario_mas_horas]
    
    # Agrupar por año y sumar las horas jugadas
    sumas_por_anio = df_usuario_mas_horas.groupby('release_year')[genero].sum()

    


    return {
        "Usuario con más horas jugadas del genero": usuario_mas_horas,
        "Horas jugadas": sumas_por_anio.to_dict()       
    } 
    
    
@app.get('/best_developer_year/') 
def best_developer_year( año : int ):
    
    df_b_dev=pd.read_csv('4punto.csv')

    
    df_filt = df_b_dev.loc[(df_b_dev['year'] == año)]
    
    df_agrupado = df_filt.groupby('developer').size().reset_index(name='repeticiones')
    
    df_top3 = df_agrupado.sort_values('repeticiones', ascending=False).head(3)
    
    resultado = [{"Puesto " + str(i + 1): row['developer']} for i, (_, row) in enumerate(df_top3.iterrows(), start=0)]
    
    return resultado
