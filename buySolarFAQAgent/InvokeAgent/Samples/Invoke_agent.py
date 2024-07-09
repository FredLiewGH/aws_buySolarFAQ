# import boto3
# import json
# import botocore.exceptions

# def lambda_handler(event, context):

#     # INVOKE AGENT
#     agent_id = "LK9KW15QJO"
#     agent_alias_id = "EHJOODDOPG"
#     session_id = "12345"
#     prompt = "I cannot login to my account."
#     agents_runtime_client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")
    
#     try:
#         # Note: The execution time depends on the foundation model, complexity of the agent,
#         # and the length of the prompt. In some cases, it can take up to a minute or more to
#         # generate a response.
        
#         response = agents_runtime_client.invoke_agent(
#             agentId=agent_id,
#             agentAliasId=agent_alias_id,
#             sessionId=session_id,
#             inputText=prompt,
#         )
    
#         completion = ""
    
#         for event in response.get("completion"):
#             chunk = event["chunk"]
#             completion = completion + chunk["bytes"].decode()

#     except ClientError as e:
#         print(f"ERROR: Can't invoke agent '{agent_id}'. Reason: {e}")
#         logger.error(f"Couldn't invoke agent. {e}")
#         raise
#         exit(1)
    
#     print(completion)
#     return completion
