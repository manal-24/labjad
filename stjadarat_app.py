import streamlit as st
from PIL import Image

# Load the image
image = Image.open('region2022.png')
image2 = Image.open('region2023.png')

st.write('a')
st.markdown("<h1 style='text-align: center;'>المناطق الأكثر توظيفاً في المملكة بين عامي 2022 و2023</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>تسعى المملكة إلى توفير فرص العمل عبر موقع جدارات لتسهيل عملية البحث للباحثين عن العمل. تعتبر منصة **جدارات** الوطنية الموحدة للتوظيف أداة فعالة تهدف إلى تحسين آلية إعلان الوظائف في جميع القطاعات، مما يسهل على الباحثين عن عمل الوصول إلى الفرص المتاحة</h5>", unsafe_allow_html=True)

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=500)  # Center the image in the second column


with col3:
    st.write("")  # Empty space in the third column
st.write('ops')

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image2, width=500)


with col3:
    st.write("")  # Empty space in the third column

