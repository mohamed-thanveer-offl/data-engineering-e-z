# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
#read csv
    df1=pd.read_csv(uploaded_file)