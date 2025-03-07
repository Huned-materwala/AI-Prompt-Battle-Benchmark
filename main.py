# main.py
from src.ai_models import AIModel
import argparse
from src.battle_engine import run_battle
from src.evaluation import judge_battle

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="AI vs AI Prompt Battle")
    parser.add_argument("--ai1", type=str, required=True, help="Name of the first AI model")
    parser.add_argument("--ai2", type=str, required=True, help="Name of the second AI model")
    parser.add_argument("--prompt", type=str, required=True, help="The prompt for the AI battle")

    # Parse arguments
    args = parser.parse_args()

    # Run a battle between the two AIs
    response1, response2 = run_battle(args.ai1, args.ai2, args.prompt)

    # Judge the battle based on the responses
    winner = judge_battle(response1, response2)
    print(f"Winner: {winner}")

if __name__ == "__main__":
    main()
