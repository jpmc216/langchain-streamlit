import streamlit as st


# Initialize session state variables
if 'openai_api_key' not in st.session_state:
	st.session_state.openai_api_key = ""

st.set_page_config(page_title="Home", page_icon="🦜️🔗", layout="wide")

st.header("Analyze Data using Langchain🦜️ and Open AI🤖 ")

st.markdown(
    """
    [LangChain](https://langchain.readthedocs.io/en/latest) is an open-source framework created to aid the development of applications leveraging the power of large language models (LLMs).

    **👈 Provide the API keys in Setup, and proceed with steps from the sidebar.**

    * A sample app for analyzing data using LangChain and Open AI.
    * References: Blog | [Source Code](https://github.com/jpmc216/langchain-streamlit)   
    """
)
