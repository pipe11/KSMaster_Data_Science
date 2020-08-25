
import streamlit as st 
import altair as alt
import pandas as pd

life = pd.read_csv("https://raw.githubusercontent.com/rezpe/datos_viz/master/lifecountries.csv")

chart_life = alt.Chart(life).mark_circle().encode(
    x='Country GDP',
    y='Life Expectancy',
    size='size',
    color='Continent',
    tooltip='country'
).interactive()

st.title("Esperanza de vida según el pais")

st.markdown("Hemos registrado la espearnza de vida y la renta per capita en varios paises, y hemos hecho un gráfico")

st.write(chart_life)
