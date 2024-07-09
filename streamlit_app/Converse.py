import os
import uuid
import requests
import json
import random

# Write conversation to file
# def writeToFile(filedir, filename, content, logger):
#     try:
#         if not os.path.exists(filedir): 
#             os.makedirs(filedir) 
    
#         filepath = os.path.join(filedir, filename)    
#         with open(filepath, "a") as myfile:        
#             myfile.write(f"{content}\n\n")

#         logger.info(f"Write to file: {filepath}")
#     except Exception as e:
#         logger.exception(f"Error write to file: {e}", exc_info=True)


# def getThankResponse(logger):
#     try:
#         filepath = "buySolarFAQAgent/streamlit_app/General_Responses_Thank_v1.0.txt"
#         with open(filepath, "r") as myfile:        
#             lines = myfile.readlines()

#             if lines.__len__ == 0:
#                 return "You're welcome! Is there anything else I can help you with?"
#             else:
#                 return (random.choice(lines))
#     except Exception as e:
#         logger.exception(f"Error read from response file: {e}", exc_info=True) 


def startChat():
    url = "https://5gldi32bl5.execute-api.us-east-1.amazonaws.com/buySolar/func_buySolar_FAQ"    

    # Write to chat history file
    session_id = uuid.uuid4().hex    
    # file_chatDir = "buySolarFAQAgent/streamlit_app/ChatHistory"
    # file_chatHist = f"{session_id}.txt"
    # writeToFile(file_chatDir, file_chatHist, f"Start Chat Session ID: {session_id}", logger)

    greetMsg = "Bot: Hello! Welcome to buySolar. How may I help you?"
    print(f"{greetMsg}\n")
    # writeToFile(file_chatDir, file_chatHist, greetMsg, logger)
    
    while True:
        prompt = input("Human: ")
        # writeToFile(file_chatDir, file_chatHist, F"Human: {prompt}", logger)

        ### Hardcoded response due to prompt script unable to return the correct response to thank
        if "thank" in prompt.lower():
            # thankMsg = getThankResponse(logger)
            thankMsg = "No problem at all! Thank you for choosing buySolar. We value your business and are committed to providing excellent customer service. Is there anything else I can help with today?"
            print(f"\n{thankMsg}\n")
            # writeToFile(file_chatDir, file_chatHist, thankMsg, logger)
        else:
            payload = json.dumps({
                "prompt": prompt,
                "sessionId": session_id
            })
            
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)

            respondMsg = f"Bot: {response.text}"
            print(f"\n{respondMsg}\n")
            # writeToFile(file_chatDir, file_chatHist, respondMsg, logger)
