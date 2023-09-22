from main import *

st.set_page_config(page_title="ChatBot Entel", page_icon="📱")
st.title("📱ChatBot Entel")

def conversational_chat(query):
    result = qa({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

 # Initialize messages
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["¡Hola! Bienvenido al chat de Entel. ¿En que te puedo ayudar?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hola!"]
# Create containers for chat history and user input
response_container = st.container()
container = st.container()

# User input form
with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Pregunta:", placeholder="¿En que te puedo ayudar?", key='input')
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button and user_input:
        output = conversational_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

# Display chat history
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            st.markdown(message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile"))
            st.markdown(message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs"))