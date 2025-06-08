==============================
AI-to-AI Text Conversation Bot
==============================

📚 Overview
-----------
This project simulates a conversation between two AI agents using a text-based loop.
Each AI agent takes turns responding to the other's output, creating an ongoing dialog.

Ideal for experimentation, humor, AI behavior studies, or prompt engineering.

💡 Features
-----------
- Simulates two conversational AI agents
- Customizable agent personalities
- Loop-based conversation system
- Easy to configure and extend

🛠 Requirements
---------------
- Python 3.8+
- OpenAI Python SDK (`openai`)
- (Optional) `.env` file to store your API key

📦 Installation
---------------
1. Clone the repository:
   git clone https://github.com/yourusername/ai-to-ai-conversation.git

2. Navigate into the project directory:
   cd ai-to-ai-conversation

3. Install dependencies:
   pip install -r requirements.txt

4. Set your OpenAI API key:
   - Create a `.env` file:
     OPENAI_API_KEY=your-api-key-here

🧠 How It Works
---------------
- The script initializes two AI agents.
- You can customize their system prompts (e.g., "You are a wise philosopher" vs "You are a curious child").
- The loop passes the response from one agent as input to the other, repeating until a defined turn limit is reached.

🚀 Usage
--------
Run the conversation script:

   python ai_conversation.py

Edit the `ai_conversation.py` file to:
- Change agent roles
- Modify number of turns
- Alter conversation logic

📝 Example Output
-----------------
AI1: Hello, who are you?
AI2: I am an AI designed to learn through conversation. And you?
AI1: I am a digital thinker, trained on the philosophies of mankind...

🛠 Configuration
----------------
You can configure the following in `config.py`:
- Number of conversation turns
- Agent personalities
- Model version (e.g., gpt-4 or gpt-3.5-turbo)

🙌 Contributing
---------------
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📄 License
----------
MIT License

🧠 Author
---------
Created by [Your Name]

GitHub: https://github.com/yourusername/ai-to-ai-conversation
