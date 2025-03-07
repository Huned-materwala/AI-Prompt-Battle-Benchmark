import requests
from huggingface_hub import hf_hub_download
from dotenv import load_dotenv
import os

load_dotenv()  # Load API keys from .env file

class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_response(self, prompt):
        return self.call_huggingface(prompt)

    def call_huggingface(self, prompt):
        api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
        headers = {
            "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
        }
    
        try:
            response = requests.post(api_url, headers=headers, json={"inputs": prompt})
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.text)  # Full response content for debugging
            if response.status_code == 200:
                return response.json()[0]['generated_text']
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Request failed: {str(e)}"

# Example Usage
ai1 = AIModel("openai-community/gpt2")
ai2 = AIModel("openai/whisper-small")  # Example for Google Gemini model (if API is available)

print(ai1.generate_response("What is the meaning of life?"))
print(ai2.generate_response("What is the meaning of life?"))
