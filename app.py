import streamlit as st

# Custom imports
from multipage import MultiPage
from sites import Overview, Arosa, Meiringen
from PIL import Image


# Create an instance of the app
app = MultiPage()

# Title of the main page
col1, col2 = st.columns(2)

with col1:
    st.title("Sustainable Analytics")

with col2:
    image = Image.open("sites/images/overview.jpg")
    st.image(image)

st.write("______")

# Add all your applications (sites) here
app.add_page("Overview", Overview.app)
app.add_page("Arosa", Arosa.app)
app.add_page("Meiringen/Hasliberg", Meiringen.app)


# The main app
app.run()

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>created by Daniel Leibrock, Remo Kälin and Simon Glauser for SUA01</p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)




