import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# @st.cache
def app():
    # create overview dashboard
    st.header("Our Project")
    st.write("This Dashboard explains what makes our project unique and how this could help deezer to also incorporate content based recommendation into the existing system. We created three different Recomender Systems, all of which take different approaches. These systems can be analyzed and combined to support many users with the desired suggestions.")
    st.write("---------")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Arosa")
        image = Image.open("images/arosa.jpg")
        st.image(image)
        data = {'Info': ['Canton', 'Population', 'Elevation', 'Website'],
                ' ': ["Grisons", "3'132", "1'775 m.a.s.l.", "https://www.gemeindearosa.ch"]}
        df = pd.DataFrame(data)
        st.dataframe(df)

    with col2:
        st.subheader("Meiringen/Hasliberg")
        image = Image.open("images/meiringen.jpg")
        st.image(image)
        data = {'Info': ['Canton', 'Population', 'Elevation', 'Website'],
                ' ': ["Bern", "4'666", "595 m.a.s.l.", "https://www.meiringen.ch"]}
        df = pd.DataFrame(data)
        st.dataframe(df)
    st.write("---------")

    st.title("Location in Switzerland")

    df = pd.DataFrame(
        np.array([[46.7283584, 8.1920768], [46.7835735, 9.6785172]]),
        columns=['lat', 'lon'])

    st.map(df)
    st.write("---------")

