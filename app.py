import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})


st.title("Le café des quatre")
st.write("Voici un diagramme d'une vague sinus quelconque pour absolument aucune raison.") 
st.altair_chart(alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
))

st.header("MENU (selon les messages discord):")
"""
🧈 ---- 1,25$ \n
🥥 ---- 1,00$\n
🫐 ---- gratuit\n
☕ ---- gratuit\n
🍒 ---- gratuit\n
🍩 ---- 0,01$\n
🧀  ---- 0,50$/morceau\n
🍓  ---- gratuit\n
🍨  ---- 3,50$\n
🥨  ----  Petit: 1,50$; Grand: 2,75$\n
🥐  ---- 1,75$\n
🍰  ---- 3,75$\n
🥖 ---- gratuit\n
🍵  ---- 1,50$\n
"""
"""

"""

st.header("Liste de proverbes: À ajouter")

st.header("Liste de néologismes communautaires: À compléter")
"""
**1. Cunidé(e)**: fusion de aucune et idée. 

a) Lorsqu'on le dit juste comme ça c'est pour désigner qu'on a aucune idée sur quelque chose.
Ex. -Tsais-tu ce qu'est l'identité d'euler? -cunidée.

b) Lorsqu'on l'utilise sur quelqu'un, ça veut dire qu'il est mal informé tout le temps.
Ex. -Le gars savait pas qu'il y avait un exam de lecture lundi. Quel cunidé.

En effet, lorsque nous utilisons la première définition trop souvent, nous devenons ce qu'est la deuxième définition.
"""


