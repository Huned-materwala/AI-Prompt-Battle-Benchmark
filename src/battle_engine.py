from src.ai_models import AIModel

def run_battle(ai1_name, ai2_name, prompt):
    ai1 = AIModel(ai1_name)
    ai2 = AIModel(ai2_name)

    response1 = ai1.generate_response(prompt)
    response2 = ai2.generate_response(prompt)

    print(f"AI 1 ({ai1_name}): {response1}")
    print(f"AI 2 ({ai2_name}): {response2}")

    return response1, response2

# Example battle
prompt = "What is the meaning of life?"
run_battle("openai-community/gpt2", "openai/whisper-small", prompt)
