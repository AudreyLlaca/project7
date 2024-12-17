import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos en un DataFrame
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un encabezado
st.header("Check out the car data)

# Crear un botón
hist_button = st.button("Build Histogram")

# Crear el histograma cuando se haga clic en el botón
if hist_button: 
    st.write("check out the dataset for the car sells")
    
    # Generar el histograma usando Plotly Express
    fig = px.histogram(car_data, x="odometer", title="Histogram")
    
    # Mostrar el gráfico Plotly en la app de Streamlit
    st.plotly_chart(fig, use_container_width=True)
