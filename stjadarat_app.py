import streamlit as st
from PIL import Image

# Load the image
image = Image.open('region2022.png')
image2 = Image.open('region2023.png')

st.write('a')
st.markdown("<h1 style='text-align: center;'>المناطق الأكثر توظيفاً في المملكة بين عامي 2022 و2023</h1>", unsafe_allow_html=True)

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=200)  # Center the image in the second column
    st.image(image2, width=200)


with col3:
    st.write("")  # Empty space in the third column

