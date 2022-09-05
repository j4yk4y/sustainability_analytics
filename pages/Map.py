import streamlit as st
import pandas as pd
import numpy as np

#@st.cache
def app():
    st.title("Map of Switzerland")

    df = pd.DataFrame(
        np.array([[46.8206, 8.0339], [46.7493333, 8.2367225], [46.6324537, 8.5918333]]),
        columns=['lat', 'lon'])

    st.map(df)


    #Visualisation
    option = st.selectbox(
        'Please choose a character?',
        ("Skigebiet 1","Skigebiet 2", "Skigebiet 3"))

    st.write('You selected:', option)





