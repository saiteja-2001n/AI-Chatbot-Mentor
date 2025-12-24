# 🤖 AI Chatbot Mentor (Streamlit + LangChain)
AI Chatbot Mentor is a module-specific intelligent learning assistant built using Streamlit and LangChain.
Unlike generic chatbots, this application strictly responds only within the selected learning module, ensuring focused, relevant, and distraction-free guidance.

## 🚀 Features
🔹 Module-based mentoring (Python, SQL, ML, EDA, etc.)
🔹 Context-aware conversational responses
🔹 Strict domain control per module
🔹 Interactive Streamlit UI
🔹 Session-based chat history
🔹 Option to reset or switch learning modules

## 🛠️ Tech Stack
- Frontend / UI: Streamlit
- LLM Orchestration: LangChain
- Language Model: Gemini (Google Generative AI)
- Backend: Python
- Version Control: Git & GitHub

## 📁 Project Structure
AI-Mentor/
├── chatbot/
│   ├── app.py
│   ├── utils.py
│   ├── prompts.py
│   └── modules/
├── .gitignore
├── README.md
├── requirements.txt


## 🧠 How It Works
- User selects a learning module
- Chatbot restricts responses to the chosen domain
- LangChain manages prompt context and conversation flow
- Responses are generated using Gemini LLM
- Session state preserves chat history until reset

## 🔐 Security & Best Practices
- API keys stored using environment variables
- Virtual environment excluded via .gitignore
- Clean Git history with meaningful commits

## 📌 Use Cases
- Students learning technical subjects
- Focused interview preparation
- Guided self-learning
- AI-assisted mentoring platforms

## 📈 Future Enhancements
- User authentication
- Chat export feature
- Module-wise quizzes
- Multi-LLM support
- Deployment on Streamlit Cloud / Hugging Face Spaces
