import streamlit as st

from streamlit_option_menu import option_menu

import extract, load, transform
st.set_page_config(
        page_title="Data Engineering E Z",
)

import pandas as pd
# import streamlit as st

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
#read csv
    df = pd.read_csv(uploaded_file)

    headers = df.columns

    st.write(headers)