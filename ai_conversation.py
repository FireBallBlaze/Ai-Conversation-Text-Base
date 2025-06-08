import openai
import os
from config import AGENT1_SYSTEM_PROMPT, AGENT2_SYSTEM_PROMPT, MODEL, NUM_TURNS
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )
    return response['choices'][0]['message']['content']

def main():
    print("Starting AI-to-AI Conversation...\n")
    ai1_messages = [{"role": "system", "content": AGENT1_SYSTEM_PROMPT}]
    ai2_messages = [{"role": "system", "content": AGENT2_SYSTEM_PROMPT}]

    # Start with a simple greeting
    initial_message = "Hello, who are you?"
    ai1_messages.append({"role": "user", "content": initial_message})
    ai1_reply = chat_with_ai(ai1_messages)
    print("AI1:", ai1_reply)
    ai2_messages.append({"role": "user", "content": ai1_reply})

    for i in range(NUM_TURNS):
        ai2_reply = chat_with_ai(ai2_messages)
        print("AI2:", ai2_reply)
        ai1_messages.append({"role": "user", "content": ai2_reply})

        ai1_reply = chat_with_ai(ai1_messages)
        print("AI1:", ai1_reply)
        ai2_messages.append({"role": "user", "content": ai1_reply})

if __name__ == "__main__":
    main()
