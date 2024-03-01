import streamlit as st
import pandas as pd


original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
st.markdown(original_title, unsafe_allow_html=True)


# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)






main_page = st.button("หน้าแรก")
if main_page:
    st.write("ไปยังหน้าแรก")


st.header(":red[องค์การนักศึกษา]", divider='blue')
st.title(":blue[องค์การนักศึกษา]")
st.title("มหาวิทยาลัยอุบลราชธานี")
st.markdown("<span style='color: yellow;'> มหาวิทยาลัยอุบลราชธานี</span>", unsafe_allow_html=True)

# main_page = st.button("หน้าแรก")
# if main_page:
#     st.write("ไปยังหน้าแรก")