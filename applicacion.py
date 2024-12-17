import streamlit as st
import pandas as pd
import plotly.express as px
import os 

#por problema en Render añadiremos las siguientes lineas de codigo para detectar el puerto
port = int(os.environ.get("PORT", 8501))
st._config.set_option("server.port", port)

port = int(os.environ.get("PORT", 8501))

car_data = pd.read_csv('notebooks/vehicles_us.csv')


st.header("Check out the car data")


hist_button = st.button("Build Histogram")

#Boton1
if hist_button: 
    st.write("Check out the dataset for the car sells")
    
   
    fig = px.histogram(car_data, x="odometer", title="Histogram")
    
  
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Build scatter plot")
#boton2
if scatter_button:
    st.write("Scatter plot between the price and odometer")
    
    
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        title="Price vs Odometer",
        labels={"odometer", "price USD"}
    )
    
   
    st.plotly_chart(fig_scatter, use_container_width=True)
