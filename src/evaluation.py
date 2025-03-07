from src.ai_models import AIModel

def judge_battle(response1, response2):
    prompt = f"""
    Compare these AI responses and declare a winner.

    Response 1: {response1}
    Response 2: {response2}

    Judge the responses based on clarity, relevance, and creativity.
    """

    judge = AIModel("xlnet/xlnet-base-cased")
    verdict = judge.generate_response(prompt)
    return verdict

# Example:
winner = judge_battle("AI 1 response...", "AI 2 response...")
print("Judgment:", winner)
