import boto3, json

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

initial_message = {
    "role": "user",
    "content": [
        {
          "text": "\n\nHuman:\n<text>\n Faye: Hi Lydia!\n Lydia: Hi Faye! Have you recieved the replacement cable that I ordered for you? \n Faye: No I did not, did you send to my new address? \n Lydia: I mailed it to 41 Oak Street, Bristol, U.K.\n Faye: That is my old address, my new address since last week is 105 Lionel Road, London, W8 9YD, U.K.\n Lydia: Please can you give me your new phone number as well?\n Faye: Sure, it's 019377464944 </text> \n\nRemove all personally identifying information from the text and replace it with “xxx”. All names, phone numbers, and email addresses must get replaced with xxx. \n\nPlease provide the sanitized version of the text with all PII removed in <response></response> XML tags.\n\nAssistant:"
        }
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId="anthropic.claude-v2",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2048,
        "temperature": 0,
        "topP": 1
    },
)

response_message = response['output']['message']
print(json.dumps(response_message, indent=4))
