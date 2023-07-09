import streamlit as st

from streamlit_extras.switch_page_button import switch_page
    
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
    else:
        st.session_state.openai_api_key = openai_api_key
        
#next_page = st.button("Next")
# if next:
#     switch_page("Upload_CSV")