import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.title("Exploración de la base de datos de vehículos usados")
st.subheader("Proyecto del Sprint 7")

st.write(
    "El código está alojado en este [repositorio](https://github.com/naibafomsare/sprint7) de GitHub.")

st.divider()  # Draws the horizontal line

st.write('Seleccione la opción deseada:')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

# crear otra casilla de verificación
build_scatter = st.checkbox('Construir un diagrama de dispersión')

# Lógica a ejecutar cuando se marca la casilla del histograma
if build_histogram:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Lógica a ejecutar cuando se marca la casilla del gráfico de dispersión
if build_scatter:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                    y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
