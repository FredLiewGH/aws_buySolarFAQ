# import boto3
# import json
# import botocore.exceptions

# def lambda_handler(event, context):
#     # TODO implement
#     # return {
#     #     'statusCode': 200,
#     #     'body': json.dumps('Hello from Lambda!')
#     # }
    
#     # Create a Bedrock Runtime client in the AWS Region of your choice.
#     bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
#     # Set the model ID, e.g., Claude 3 Haiku.
#     model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    
#     # Define the prompt for the model.
#     prompt = "Why is the sky blue?"
    
#     # Format the request payload using the model's native structure.
#     native_request = {
#         "anthropic_version": "bedrock-2023-05-31",
#         "max_tokens": 512,
#         "temperature": 0.5,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [{"type": "text", "text": prompt}],
#             }
#         ],
#     }
    
#     # Convert the native request to JSON.
#     request = json.dumps(native_request)
    
#     # # INVOKE MODEL WITH RESPONSE STREAM
#     # streaming_response = bedrock_client.invoke_model_with_response_stream(
#     #     modelId=model_id, body=request
#     # )
    
#     # # Extract and print the response text in real-time.
#     # for event in streaming_response["body"]:
#     #     chunk = json.loads(event["chunk"]["bytes"])
#     #     if chunk["type"] == "content_block_delta":
#     #         print(chunk["delta"].get("text", ""), end="")
            

#     try:
#         # INVOKE MODEL
#         response = bedrock_client.invoke_model(modelId=model_id, body=request)
    
#     except (ClientError, Exception) as e:
#         print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
#         exit(1)
    
#     # Decode the response body.
#     model_response = json.loads(response["body"].read())
    
#     # Extract and print the response text.
#     response_text = model_response["content"][0]["text"]
#     print(response_text)
#     return response_text
