import uuid
import requests
import json
import random
import time
import re
import streamlit as st


# Streamed response emulator
def response_stream(response):
    my_list = re.findall(r"\S+|\n", response)
    for word in my_list:
        yield word + " "
        time.sleep(0.05)


# Streamed response emulator
def response_thank():
    response = random.choice(
        [
            "You're very welcome! I'm happy I could help. Please let me know if there's anything else I can assist you regarding solar panels or our services.",
            "No problem at all! Thank you for choosing buySolar. We value your business and are committed to providing excellent customer service. Is there anything else I can help with today?",
            "You're welcome! Glad I could be of service, please reach out to us if there's more inquiries. Is there anything else I could help you with?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def startChat():
    url = "https://5gldi32bl5.execute-api.us-east-1.amazonaws.com/buySolar/func_buySolar_FAQ"        
    session_id = uuid.uuid4().hex    
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["content"] != None:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])    

    if prompt := st.chat_input("Say Something"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        ### Hardcoded response due to prompt script unable to return the correct response to thank
        with st.chat_message("assistant"):
            if "thank" in prompt.lower():            
                response = st.write_stream(response_thank())                
            else:
                payload = json.dumps({
                    "prompt": prompt,
                    "sessionId": session_id
                })
                
                headers = {
                    'Content-Type': 'application/json'
                }
                return_request = requests.request("POST", url, headers=headers, data=payload)
                response = st.write_stream(response_stream(return_request.text))
                
            st.session_state.messages.append({"role": "assistant", "content": response})
