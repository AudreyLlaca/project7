import streamlit as st
import pandas as pd
import plotly_express as px

# Leer los datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header("Aplicación de Streamlit para visualización de datos de coches")

# Crear un botón
hist_button = st.button("Construir histograma")

# Crear el histograma cuando se haga clic en el botón
if hist_button: 
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    
    # Generar el histograma usando Plotly Express
    fig = px.histogram(car_data, x="odometer", title="Histograma del odómetro")
    
    # Mostrar el gráfico Plotly en la app de Streamlit
    st.plotly_chart(fig, use_container_width=True)
