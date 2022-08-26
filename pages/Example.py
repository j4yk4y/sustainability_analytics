import pandas as pd
import streamlit as st
from PIL import Image

#@st.cache
def app():
    st.title("Example Example")
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open("images/overview.png")
        st.image(image)

    with col2:
        st.write("Some very interesting text.")

    st.write("--------------------")

    #Visualisation
    option = st.selectbox(
        'Please choose a character?',
        ("a","b"))

    st.write('You selected:', option)

    values = st.slider(
        'How often',
        1, 10, 5)
    st.write('Selected Number:', values)

    if st.button('Print'):
        for i in range(0, values):
            st.write(option)

    st.write("--------------------")

    df = pd.read_excel("data/Groundwater/Groundwater Escholzmatt.xlsx", index_col=0)
    st.line_chart(data=df,
                  use_container_width=True)




