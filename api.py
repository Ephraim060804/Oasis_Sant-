import os
from mistralai.client import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

AGENT_ID = "ag_019f3e51c86575dbaee9834c3686c1cc"
AGENT_VERSION = 0


message_history = []

print(" Chat avec Mistral (tapez 'quit' pour quitter)")
print("-" * 50)

while True:
    user_input = input("\nVous: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print(" Au revoir !")
        break
    
    if not user_input.strip():
        print(" Veuillez entrer un message valide")
        continue
    
    
    message_history.append({"role": "user", "content": user_input})
    
   
    
    response = client.beta.conversations.start(
        agent_id=AGENT_ID,
        agent_version=AGENT_VERSION,
        inputs=message_history,  
    )
    
   
    assistant_response = None
    if response.outputs:
        for output in response.outputs:
            if output.type == 'message.output':
                assistant_response = output.content
                print(f"Assistant: {assistant_response}")
    
   
    if assistant_response:
        message_history.append({"role": "assistant", "content": assistant_response})
    
 