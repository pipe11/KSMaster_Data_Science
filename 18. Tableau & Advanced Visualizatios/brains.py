
import streamlit as st 
import altair as alt
import pandas as pd

brain = pd.read_csv ('https://raw.githubusercontent.com/rezpe/datos_viz/master/brain.csv')

hist_brain = alt.Chart(brain).mark_bar().encode(
    x = alt.X('Brain Weight', bin = alt.Bin(maxbins = 100)),
    y = "count()"
).properties(
    title = 'distribución del peso de los cuerpos',
    width = 400
).interactive()

hist_body = alt.Chart(brain).mark_bar().encode(
    x = alt.X('Body Weight', bin = alt.Bin(maxbins = 100)),
    y = "count()"
).properties(
    title = 'distribución del peso de los cerebros',
    width = 400
).interactive()

scatter_brain_body = alt.Chart(brain).mark_point().encode(
    x = 'Brain Weight', 
    y = 'Body Weight'
).properties(
    title = 'Distribución de los pesos del cuerpo y cerebro',
    width = 800
).interactive()

brain_dash = (hist_body | hist_brain) & scatter_brain_body

st.title("Peso del cuerpo y del cerebro")

st.markdown("Hemos registrado los pesos del cuerpo y del cerebro.")

st.write(brain_dash)
