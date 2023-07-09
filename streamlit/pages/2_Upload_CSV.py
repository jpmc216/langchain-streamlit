import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")

# Set API keys from session state
openai_api_key = st.session_state.openai_api_key

# Streamlit app
st.subheader('Upload CSV')
#url = st.text_input("Enter CSV file path")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

col1, col2 = st.columns([1,1])

with col1:
    preview = st.button('Save and Preview')
# with col2:
#     next = st.button('Next')
    
if data is not None and preview:
    df = pd.read_csv(data)
    st.dataframe(df.head())
    st.session_state['df_csv'] = df
    

# if next:
#     switch_page("Train_LLM")
