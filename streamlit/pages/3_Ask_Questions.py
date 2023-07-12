import streamlit as st
from streamlit_chat import message


st.set_page_config(layout="wide")

st.subheader('Step3: Analyze data by asking questions')

pd_agent = None
submitted = None

# Get agent from session state
if 'pd_agent' in st.session_state:
    pd_agent = st.session_state.pd_agent

def wrap_text(text,numchars=100):
    lines = text.split('\n')
    for line in lines:
        while len(line) > numchars:
            space_index = line[:numchars].rfind(' ')
            if space_index == -1:  # no space found
                print(line[:numchars])
                line = line[numchars:]
            else:
                print(line[:space_index])
                line = line[space_index+1:]
        print(line)
        

def ask_df(prompt):
    val = pd_agent.run(prompt)
    return val

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 

with st.form('form', clear_on_submit=True):

    user_input = st.text_input('Type your question here: ', '', key='input')
    submitted = st.form_submit_button('Send')
    
    if not pd_agent:
        st.markdown(
            """
            ** Missing langchain agent. Restart the setup process.**

            * Check to make sure Open AI key is saved. 
            * Check to make sure CSV file is uploaded and saved
            """
        )
 
    if submitted and user_input:
        output = ask_df(user_input)
        print(output)
    
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
    
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

    