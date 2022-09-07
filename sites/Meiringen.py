import streamlit as st
import pandas as pd
import numpy as np

#@st.cache
def app():


    #Visualisation
    st.title("Meiringen / Hasliberg")

    option = st.selectbox(
        'Please choose a character?',
        ("Skigebiet 1","Skigebiet 2", "Skigebiet 3"))

    st.write('You selected:', option)





