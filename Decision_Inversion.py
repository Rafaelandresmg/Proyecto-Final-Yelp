import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

#streamlit run Desicion_Inversion.py
#python -m streamlit run Decisión_Inversion.py



#####################################################################################################################################################################################

# Crear la interfaz de usuario con Streamlit
st.title('Modelo de decisión de inversion 📈')

# Permitir al usuario introducir sus propios datos
ciudadStream = st.selectbox('Seleccione la Ciudad',
                    ('Boise','Brentwood','Carmel','Cherry Hill','Clayton','Clearwater','Clearwater Beach',
 'Dunedin','Edmonton','Exton','Fishers','Franklin','Goleta','Goodlettsville','Hamilton','Indian Rocks Beach',
 'Indianapolis','Jenkintown','Kirkwood','Largo','Levittown','Lutz','Maplewood','Marana','Media','Metairie',
 'Mooresville','Mount Laurel','Nashville','New Hope','New Orleans','Norristown','Oldsmar','Palm Harbor',
 'Philadelphia','Pinellas Park','Reno','Saint Louis','Saint Pete Beach','Saint Petersburg','Santa Barbara',
 'Sicklerville','Smyrna','Sparks','St Louis','St Petersburg','St. Louis','St. Petersburg','Tampa','Tucson',
 'Voorhees','Wayne', 'West Chester','Wilmington','Woodbury')
                    )

#####################################################################################################################################################################################

categoriasStream = ('Acai Bowls', 'Asian Fusion', 'Barbeque', 
                    'Buffets', 'Burgers', 'Cafes', 'Cafeteria', 
                    'Cajun/Creole', 'Chicken Wings', 'Child Care & Day Care', 
                    'Coffee & Tea', 'Coffee & Tea Supplies', 'Coffee Roasteries', 
                    'Comfort Food', 'Comic Books', 'Donuts', 'Empanadas', 'Fast Food', 
                    'Food', 'Food Court', 'Food Delivery Services', 'Food Stands', 'Food Tours', 
                    'Food Trucks', 'Juice Bars & Smoothies', 'Junk Removal & Hauling', 'Lounges', 
                    'Pizza', 'Pubs', 'Restaurants', 'Salad', 'Sandblasting', 'Sandwiches', 
                    'Seafood', 'Specialty Food', 'Steakhouses', 'Tacos', 'Vegan', 'Vegetarian')
categorias_seleccionadas = st.multiselect('Seleccione hasta tres categorías', categoriasStream,max_selections=3)

#####################################################################################################################################################################################

# Si el botón es presionado, mostrar un texto
boton = st.button('Predecir')
if boton :
# Aca se pone el modelo



    st.title('La predicción del modelo es:')
# 1) Lectura y transformaciones
# Data Frame De Business Filtrado
    businessML1 = 'ModeloML1/dataBusinesML1.csv'
    # Lee el archivo CSV en un DataFrame
    dfBusinessML1 = pd.read_csv(businessML1)
    rutaReview= "ModeloML1/review_con100000.csv"    
    dfReviewYelp = pd.read_csv(rutaReview, nrows=100000)
    dfReviewYelp['user_id'] = dfReviewYelp['user_id'].str.strip()
    dfReviewYelp['review_id'] = dfReviewYelp['review_id'].str.strip()
    dfReviewYelp = dfReviewYelp[['business_id','stars']]
    # 2) Merges 
    # Union de tablas
    merge1 = dfBusinessML1.merge(dfReviewYelp, on='business_id', how='inner')
    #Dummies Ciudad
    merge2 = pd.get_dummies(merge1, columns=['city'], prefix='', prefix_sep='')
    mergeBusinessMl1ReviewYelp= merge2.drop(columns=['business_id', 'name','address','state'])
    mergeBusinessMl1ReviewYelp = mergeBusinessMl1ReviewYelp.astype(int)#aca se ejecuta el modelo
    

# 3) Modelo 


# Leer el DataFrame 'df' desde tu fuente de datos
# ...

# Definir las categorías y la ciudad
    categorias = ['Pizza', 'Burgers', 'Cafes'] 
    ciudad = 'Boise'

    X = mergeBusinessMl1ReviewYelp.drop(columns=['stars'])
    y = mergeBusinessMl1ReviewYelp['stars']

    # Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar y entrenar el modelo de árbol de decisión
    modelo = DecisionTreeRegressor()
    modelo.fit(X_train, y_train)

    # Predecir las etiquetas en el conjunto de prueba
    y_pred = modelo.predict(X_test)

    def predecir_cantidad_estrellas(categorias, ciudad, modelo):
        # Crear un DataFrame con todas las características existentes
        datos = X_test.copy()
        
        # Establecer las características binarias correspondientes a las categorías y la ciudad
        for categoria in categorias:
            datos[categoria] = 1
        datos[ciudad] = 1
        
        # Predecir la cantidad de estrellas utilizando el modelo
        cantidad_estrellas = modelo.predict(datos)
        
        # Calcular el promedio de las predicciones
        promedio_estrellas = cantidad_estrellas.mean()
        return promedio_estrellas

    # Ejemplo de uso
    categorias = categorias_seleccionadas
    ciudad = ciudadStream
    cantidad_estrellas = predecir_cantidad_estrellas(categorias, ciudad, modelo)
    # Menor a 10
    promedio_estrellas_por_ciudad = merge1.groupby('name')['stars'].mean().mean()
        
    if cantidad_estrellas >= 0.95 * promedio_estrellas_por_ciudad:
        recomendacion = True
    else:
        recomendacion = False

#####################################################################################################################################################################################

    valor = cantidad_estrellas
    st.text('el numero de ⭐ predichas es: ' + str(valor))

    if recomendacion:
        st.text('SI se recomienda invertir ✔️')
    else: 
        st.text('NO se recomienda invertir ❌')