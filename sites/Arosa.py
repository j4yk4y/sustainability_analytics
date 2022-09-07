import streamlit as st
from PIL import Image

#@st.cache
def app():
    st.title("Arosa")
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open("images/arosa.jpg")
        st.image(image)

    with col2:
        st.subheader("Overall")
        st.write("Some very interesting text.")

    st.write("--------------------")

    st.title("Snow")

    st.write("--------------------")

    st.title("Overnight Stays")

    st.subheader("Overnight Stays 2013 - 2022")

    image = Image.open("output/overnight_chart.png")
    st.image(image)

    image = Image.open("output/overnight_decomp.png")
    st.image(image)

    image = Image.open("output/overnight_tsa.png")
    st.image(image)

    st.subheader("Season Comparison")
    option = st.selectbox(
        'Please choose a season?',
        ("Summer","Winter"))

    if option == "Summer":
        image = Image.open("output/overnight_summer.png")
        st.image(image)
        image = Image.open("output/overnight_summer_trend.png")
        st.image(image)
    elif option == "Winter":
        image = Image.open("output/overnight_winter.png")
        st.image(image)
        image = Image.open("output/overnight_winter_trend.png")
        st.image(image)
    else:
        st.warning("something went wrong.")

    st.write("--------------------")





