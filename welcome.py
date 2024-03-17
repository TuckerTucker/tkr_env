import requests
from openai import OpenAI
from colorama import Fore, init
from dotenv import load_dotenv
import os

init()  # Initialize colorama
load_dotenv()  # Load environment variables from .env file

# URLs and API keys
base_url = "http://localhost:1234/v1"
lmstudio_api_key = "sk-not-required-lorem-ipsum"
lmstudio_model_name = "LM Studio doesn't use this yet."

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_model_name = "gpt-3.5-turbo"

def is_server_active():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            return True
        else:
            print(Fore.RED + f"Can't connect to local server {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Can't connect to local server.")
        return False
    
# Initialize the client based on server availability
if is_server_active():
    print(Fore.GREEN + "LMStudio online")
    api_key = lmstudio_api_key
    model_name = lmstudio_model_name
    client = OpenAI(base_url=base_url, api_key=api_key)
else:
    print(Fore.GREEN + "Using OpenAI.")
    model_name = openai_model_name
    client = OpenAI(api_key=openai_api_key)

# Function to send messages using the chosen client
def send_messages(client):
    stream = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant who only responds in bulleted lists. example: • hello (English) • hola (Español) • hallo (German) "},
            {"role": "user", "content": "respond with only a bulleted list of 'Hello' in three languages from either East Asia, South Asia, Europe, South America, Central America."}
        ],
        model=model_name,  # Use a valid model ID
        stream=True  # Enable streaming
    )
    print("\n")
    # Process the stream
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(Fore.LIGHTBLUE_EX + chunk.choices[0].delta.content, end="")
    print("\n")

# Call the function to send messages
send_messages(client)