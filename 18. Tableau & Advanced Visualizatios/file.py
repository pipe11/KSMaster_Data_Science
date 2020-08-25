
import streamlit as st 
import altair as alt
import pandas as pd
# https://docs.streamlit.io/en/stable/api.html
st.title("Locales de Madrid")

st.markdown("""La comunidad de Madrid realizo un censo de locales en el 2017, y hemos dibujado en un mapa
los bares de la zona""")

selec_text = st.sidebar.text_input("Escribir filtro de local",value="BAR")

# Altair
@st.cache
def get_data():
  data = pd.read_csv("https://github.com/rezpe/datos_viz/blob/master/locales_madrid.csv?raw=true")
  return data

locales = get_data()
sublocal = locales[locales['rotulo'].str.contains(selec_text)]

#st.dataframe(sublocal.head())
#st.table(sublocal.head())

st.markdown(f""" 
# Palabra Seleccionada: {selec_text} 

Hay {len(sublocal)} locales en Madrid con ese filtro""")

map_local = alt.Chart(sublocal).mark_point().encode(
    latitude="lat",
    longitude="lon",
    color=alt.Color("desc_distrito_local",legend=None)
)
st.write(map_local)
