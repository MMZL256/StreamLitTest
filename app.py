import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})



st.write("Hello world ahhh the floor is lava") 
st.altair_chart(alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
))

