import streamlit as st
import openai

from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide")
    
# Streamlit app
st.subheader('Step1: Setup')

if 'openai_api_key' in st.session_state:
    openai_api_key = st.session_state.openai_api_key
else:
    openai_api_key = ""

# Get API keys
openai_api_key = st.text_input("OpenAI API Key", value=openai_api_key, type="password")
st.caption("*Required for all apps; get it [here](https://platform.openai.com/account/api-keys).*")


col1, col2 = st.columns([1,1])

with col1:
    save = st.button('Save')
# with col2:
#     next = st.button('Next')

    
# If the 'Save' button is clicked
if save:
    if not openai_api_key.strip():
        st.error("Please provide the missing API keys.")

    openai.api_key = openai_api_key
    try:
        models = openai.Model.list()["data"]
        model_ids = [model['id'] for model in models]
    except Exception as e:
        print('Exception')
        model_ids = []

    if len(model_ids) < 1:
        st.error("Open AI Key provided does not work")
    else:
        st.session_state.openai_api_key = openai_api_key
        st.success("Open AI Key validated and saved")
        
#next_page = st.button("Next")
# if next:
#     switch_page("Upload_CSV")