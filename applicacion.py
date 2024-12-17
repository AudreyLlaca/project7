import streamlit as st
import pandas as pd
import plotly.express as px
import os 

#por problema en Render añadiremos las siguientes lineas de codigo para detectar el puerto
port = int(os.environ.get("PORT", 8501))
st._config.set_option("server.port", port)

car_data = pd.read_csv('notebooks/vehicles_us.csv') 


st.header("Check out the car data below!")


# Opcional, pero añadeas por criterio de evaluacion
show_histogram = st.checkbox("Show histogram")
show_scatterplot = st.checkbox("Show scatter plot")


if show_histogram:
    st.write("**Histogram of the odometer**")
    fig_hist = px.histogram(car_data, x="odometer", title="Histogram of the odometer")
    st.plotly_chart(fig_hist, use_container_width=True)


if show_scatterplot:
    st.write("**Sacatterplot for price and odometer**")
    fig_scatter = px.scatter(
        car_data, x="odometer", y="price", title="Scatterplot for Price vs Odometer"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)