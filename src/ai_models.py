import openai
import anthropic
import requests
from huggingface_hub import hf_hub_download
from dotenv import load_dotenv
import os

load_dotenv()  # Load API keys from .env file

class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_response(self, prompt):
        if "gpt" in self.model_name:
            return self.call_openai(prompt)
        elif "claude" in self.model_name:
            return self.call_anthropic(prompt)
        elif "gemini" in self.model_name:
            return self.call_google_gemini(prompt)
        elif "huggingface" in self.model_name:
            return self.call_huggingface(prompt)
        else:
            return "Unknown model"

    def call_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

    def call_anthropic(self, prompt):
        client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.completions.create(model=self.model_name, prompt=prompt)
        return response["completion"]

    def call_google_gemini(self, prompt):
        # Placeholder for Google Gemini API call (assuming an API is available)
        # For the sake of this example, we are making a simple request to an API endpoint
        api_url = "https://api.google.com/gemini"  # This is just an example, replace it with the real URL.
        headers = {
            "Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}",
        }
        response = requests.post(api_url, json={"prompt": prompt}, headers=headers)
        return response.json().get("response", "Error")

    def call_huggingface(self, prompt):
        # Using Hugging Face's Inference API
        api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
        headers = {
            "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
        }
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return f"Error: {response.status_code}"

# Example Usage
ai1 = AIModel("gpt-4")
ai2 = AIModel("claude-v1")
ai3 = AIModel("huggingface/distilbert-base-uncased")
ai4 = AIModel("google-gemini")  # Example for Google Gemini model (if API is available)

print(ai1.generate_response("What is the meaning of life?"))
print(ai2.generate_response("Explain black holes in simple terms."))
print(ai3.generate_response("What is the future of AI?"))
print(ai4.generate_response("Describe the future of humanity in 100 years."))
