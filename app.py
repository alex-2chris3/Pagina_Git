import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Gráfico interactivo con Plotly y Streamlit")

df = pd.DataFrame({
    "Días": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    "Ventas": [100, 120, 90, 140, 110]
})

st.write("Datos de prueba:")
st.dataframe(df)

fig = px.bar(df, x="Días", y="Ventas", title="Ventas Semanales")

st.plotly_chart(fig)
