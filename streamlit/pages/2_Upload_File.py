import streamlit as st
import pandas as pd
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
import os

st.set_page_config(layout="wide")

# Streamlit app
st.subheader('Step2: Upload the data file')

data = st.file_uploader("Upload a Dataset", type=["csv"])

col1, col2 = st.columns([1,1])

with col1:
    preview = st.button('Save and Preview')
# with col2:
#     next = st.button('Next')

if 'openai_api_key' in st.session_state:
    openai_api_key = st.session_state.openai_api_key  
        
if data is not None and preview:
    df = pd.read_csv(data)
    st.dataframe(df.head())
    
    # Validate inputs
    if not openai_api_key:
        st.error("Please provide the missing API keys in Settings.")
    elif df is None:
        st.error("Please upload the CSV to train the model on")
    else:
        try:
            with st.spinner("Please wait..."):
                #,agent_type=AgentType.OPENAI_FUNCTIONS,
                os.environ['OPENAI_API_KEY'] = openai_api_key
                
                pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
                if pd_agent:
                    st.success("Successfully trained the model")
                    st.session_state.pd_agent = pd_agent                    
        except Exception as e:
            st.exception(f"Exception: {e}")

