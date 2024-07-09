from Converse import startChat
import streamlit as st


# Main script 
if __name__ == '__main__':
    ##### STREAMLIT DECLARATIONS #####
    st.title("buySolar Chat-Bot")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    greetMsg = "Hello! Welcome to buySolar. How may I help you?"
    with st.chat_message("assistant"):        
        greetings = st.write(greetMsg)
        st.session_state.messages.append({"role": "assistant", "content": greetings})

    startChat()
