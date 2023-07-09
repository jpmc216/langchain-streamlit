import streamlit as st
import pandas as pd
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
import os

st.set_page_config(layout="wide")

# Streamlit app
st.subheader('Train LLM using Langchain')

if 'df_csv' in st.session_state:
    df_csv = st.session_state['df_csv']

if 'openai_api_key' in st.session_state:
    openai_api_key = st.session_state.openai_api_key    


if st.button("Train Model"):
    # Validate inputs
    if not openai_api_key:
        st.error("Please provide the missing API keys in Settings.")
    elif df_csv is None:
        st.error("Please upload the CSV to train the model on")
    else:
        try:
            with st.spinner("Please wait..."):
                #,agent_type=AgentType.OPENAI_FUNCTIONS,
                os.environ['OPENAI_API_KEY'] = openai_api_key
                
                pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df_csv, verbose=True)
                if pd_agent:
                    st.success("Successfully trained the model")
                    st.session_state.pd_agent = pd_agent                    
        except Exception as e:
            st.exception(f"Exception: {e}")
            
