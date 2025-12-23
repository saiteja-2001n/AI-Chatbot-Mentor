import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


import os 

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

st.set_page_config(
    page_title = '🤖 AI ChatBot Mentor',
    layout = 'centered'
)

Modules = [
    "Python",
    "SQL",
    "Power BI",
    "Exploratory Data Analysis (EDA)",
    "Machine Learning (ML)",
    "Deep Learning (DL)",
    "Generative AI (Gen AI)",
    "Agentic AI"
]

if 'module' not in st.session_state:
    st.session_state.module = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash-lite')


mentor_prompt = PromptTemplate(
    input_variables = ['module','question'],
    template = """
You are an AI mentor strictly limited to the domain: {module}.

Rules:
- Answer ONLY questions related to {module}.
- If the question is outside {module}, respond EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."

User Question:
{question}
"""
)

if st.session_state.module is None:
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.write("Your personalized AI learning assistant.")
    st.write("Please select a learning module to begin your mentoring session.")

    selected_module = st.selectbox("📌 Select a Module",Modules)

    if st.button('start Mentoring'):
        st.session_state.module = selected_module
        st.rerun()


else:
    st.title(f"🎯 {st.session_state.module} AI Mentor")
    st.write(f"I am your dedicated mentor for **{st.session_state.module}**.")
    st.write("How can I help you today?")

    for chat in st.session_state.chat_history:
        with st.chat_message(chat['role']):
            st.write(chat['content'])

    user_input = st.chat_input('Ask Your Question...?')

    if user_input:
        st.session_state.chat_history.append(
            {'role':'user','content':user_input}
        )
        with st.chat_message('user'):
            st.write(user_input)

        formatted_prompt = mentor_prompt.format(
            module = st.session_state.module,
            question = user_input
        )

        response = llm.invoke(formatted_prompt).content

        st.session_state.chat_history.append(
              {"role": "assistant", "content": response}
        )
        with st.chat_message("assistant"):
            st.write(response)
    
    if st.session_state.chat_history:
        conversation_text = ""
        for chat in st.session_state.chat_history:
            role = "User" if chat["role"] == "user" else "AI"
            conversation_text += f"{role}: {chat['content']}\n\n"

        st.download_button(
            label="📥 Download Conversation",
            data=conversation_text,
            file_name="ai_chatbot_mentor_conversation.txt",
            mime="text/plain"
        )

    if st.button("🔄 Change Module / Restart"):
        st.session_state.module = None
        st.session_state.chat_history = []
        st.rerun()   
            


