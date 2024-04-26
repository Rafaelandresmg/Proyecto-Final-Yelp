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
st.markdown("""
    <div style="text-align: center"> 
        <h1>Modelo de recomendacion de usuarios 🚀</h1>
    </div>
""", unsafe_allow_html=True)

UsuarioStream = st.selectbox('Seleccione el usuario',
                    ('Boise','Brentwood','Carmel','Cherry Hill','Clayton','Clearwater','Clearwater Beach',
 'Dunedin','Edmonton','Exton','Fishers','Franklin','Goleta','Goodlettsville','Hamilton','Indian Rocks Beach',
 'Indianapolis','Jenkintown','Kirkwood','Largo','Levittown','Lutz','Maplewood','Marana','Media','Metairie',
 'Mooresville','Mount Laurel','Nashville','New Hope','New Orleans','Norristown','Oldsmar','Palm Harbor',
 'Philadelphia','Pinellas Park','Reno','Saint Louis','Saint Pete Beach','Saint Petersburg','Santa Barbara',
 'Sicklerville','Smyrna','Sparks','St Louis','St Petersburg','St. Louis','St. Petersburg','Tampa','Tucson',
 'Voorhees','Wayne', 'West Chester','Wilmington','Woodbury')
                    )

st.markdown("""
    <div style="text-align: center"> 
        <h2>Locales mejor puntuados</h2>
    </div>
""", unsafe_allow_html=True)
# Crear tres columnas
col1, col2, col3 = st.columns(3)

# Colocar una tarjeta en cada columna
col1.markdown("""
    <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
        <h3><code style="color:#e694ff;">Local 1</code></h3>
        <p><code style="color:black;">Atributos</code></p>
    </div>
""", unsafe_allow_html=True)

col2.markdown("""
    <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
        <h3><code style="color:#e694ff;">Local 2</code></h3>
        <p><code style="color:black;">Atributos</code></p>
    </div>
""", unsafe_allow_html=True)

col3.markdown("""
    <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
        <h3><code style="color:#e694ff;">Local 3</code></h3>
        <p><code style="color:black;">Atributos</code></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""---""")

boton = st.button('Predecir')
if boton :
# Aca se pone el modelo
    st.title('La predicción del modelo es:')
    rcol1, rcol2, rcol3 = st.columns(3)

# Colocar una tarjeta en cada columna
    rcol1.markdown("""
        <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
            <h3><code style="color:#e694ff;">Local recomendado 1</code></h3>
            <p><code style="color:black;">Atributos</code></p>
        </div>
    """, unsafe_allow_html=True)

    rcol2.markdown("""
        <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
            <h3><code style="color:#e694ff;">Local recomendado 2</code></h3>
            <p><code style="color:black;">Atributos</code></p>
        </div>
    """, unsafe_allow_html=True)

    rcol3.markdown("""
        <div style="padding:10px; border:2px solid black; border-radius:5px; text-align: center;">
            <h3><code style="color:#e694ff;">Local recomendado 3</code></h3>
            <p><code style="color:black;">Atributos</code></p>
        </div>
    """, unsafe_allow_html=True)