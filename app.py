import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})

st.set_page_config(page_title="Café des quatre", page_icon="🍵", layout="wide")
st.title("Le café des quatre")
st.write("Voici un diagramme d'une vague sinus quelconque pour absolument aucune raison.") 
st.altair_chart(alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
))

with st.expander("Menu du café des quatre"):
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
with st.expander("Liste de proverbes"):
    st.header("Liste de proverbes: À ajouter")
with st.expander("Liste de néologismes"):
    st.header("Liste de néologismes communautaires:")
    """
    **:blue-background[1. Cunidé(e)]**: Aucune idée.
    
    Étymologie: Fusion des mots Aucune et Idée.
    
    a) Lorsqu'on le dit juste comme ça c'est pour désigner qu'on a aucune idée sur quelque chose.
    Ex. -Tsais-tu ce qu'est l'identité d'euler? -cunidée.
    
    b) Lorsqu'on l'utilise sur quelqu'un, ça veut dire qu'il est mal informé tout le temps.
    Ex. -Le gars savait pas qu'il y avait un exam de lecture lundi. Quel cunidé.
    
    En effet, lorsque nous utilisons la première définition trop souvent, nous devenons ce qu'est la deuxième définition.

    
    **:blue-background[2. Champelaïllon]**: Synonyme de champion.
    
    Étymologie: Provient d'un certain prof de science surqualifié


    **:blue-background[3. Tachybuler]**: Marcher de manière étrangement rapide.
    
    Étymologie: (grec) Tachy-, vite. + (latin) ambula, marcher.
    
    Note: Il n'est pas orthodoxe de mélanger les racines grecques et latines mais on s'en balec absolument.


    
    """







