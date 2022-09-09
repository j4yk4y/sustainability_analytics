import streamlit as st
from PIL import Image

#@st.cache
def app():
    st.title("Meiringen/Hasliberg")
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open("output/meiringen.jpg")
        st.image(image)

    with col2:
        st.title(" ")
        image = Image.open("output/meiringen_logo.png")
        st.image(image)

    st.write("--------------------")

    st.title("Snow Days")
    st.subheader("Overview 1950 - 2022")
    image = Image.open("output/Count of Snow Days in Meiringen.png")
    st.image(image, use_column_width="always")

    image = Image.open("output/TrendOfNaturalSnowMeiringen.png")
    st.image(image, use_column_width="always")

    st.write("--------------------")

    st.title("Temperature")
    st.subheader("Overview 1950 - 2022")
    image = Image.open("output/wieduwillst.png")
    st.image(image, use_column_width="always")

    st.write("--------------------")

    st.title("Overnight Stays")
    st.subheader("Overview 2013 - 2022")
    image = Image.open("output/m_overnight_chart.png")
    st.image(image)
    image = Image.open("output/m_overnight_decomp.png")
    st.image(image)
    image = Image.open("output/m_overnight_tsa.png")
    st.image(image)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('PACF'):
            image = Image.open("output/m_overnight_pacf.png")
            st.image(image)
        else:
            pass

    with col2:
        if st.button('ACF'):
            image = Image.open("output/m_overnight_acf.png")
            st.image(image)
        else:
            pass

    with col3:
        if st.button('Forecast'):
            st.info("Work in Progress")
        else:
            pass


    st.subheader("Season Comparison")
    option = st.selectbox(
        'Please choose a season?',
        ("Summer", "Winter"))

    if option == "Summer":
        image = Image.open("output/m_overnight_s_chart.png")
        st.image(image)
        image = Image.open("output/m_overnight_s_trend.png")
        st.image(image)
    elif option == "Winter":
        image = Image.open("output/m_overnight_w_chart.png")
        st.image(image)
        image = Image.open("output/m_overnight_w_trend.png")
        st.image(image)
    else:
        st.warning("something went wrong.")

    st.write("--------------------")





