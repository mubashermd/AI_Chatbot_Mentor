import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# ------------------ Streamlit Config ------------------
st.set_page_config(page_title="AI Chatbot Mentor", page_icon="🧠", layout="centered")

MODULES = ["Python", "SQL", "Power BI", "EDA", "ML", "DL", "Gen AI", "Agentic AI"]

# ------------------ Session State ------------------
if "module" not in st.session_state:
    st.session_state.module = None
if "conv" not in st.session_state:
    st.session_state.conv = []
if "memory" not in st.session_state:
    st.session_state.memory = []

# ------------------ Module Selection Screen ------------------
if st.session_state.module is None:
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.markdown("Your personalized AI learning assistant.")
    st.markdown("Please select a learning module to begin your mentoring session.")

    selected = st.selectbox("📌 Available Modules", MODULES)
    if st.button("Start Mentoring Session 🚀"):
        st.session_state.module = selected
        st.session_state.conv = []
        st.session_state.memory = [
            (
                "system",
                f"You are an expert mentor for {selected}. "
                f"Only answer questions related to {selected}. "
                f"If a question is unrelated, respond with: "
                f"'Sorry, I don’t know about this question. Please ask something related to the selected module.'",
            )
        ]
        st.rerun()

# ------------------ Mentor Chat Screen ------------------
else:
    st.header(f"🎯 {st.session_state.module} Mentor Chat")
    st.caption(f"I am your dedicated mentor for **{st.session_state.module}**. How can I help you today?")
    st.divider()

    # Display full conversation with GPT-style chat bubbles
    for msg in st.session_state.conv:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User Input
    prompt = st.chat_input("Type your question here...")
    if prompt:
        # Append user message
        st.session_state.conv.append({"role": "user", "content": prompt})
        st.session_state.memory.append(("user", prompt))
        with st.chat_message("user"):
            st.write(prompt)

        # AI Response using Gemini 2.5 Flash
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        response = model.invoke(st.session_state.memory)

        # Display AI message
        with st.chat_message("ai"):
            st.write(response.content)

        # Append AI response to session memory
        st.session_state.conv.append({"role": "ai", "content": response.content})
        st.session_state.memory.append(("ai", response.content))
        st.rerun()

    # ------------------ 📥 Download Conversation ------------------
    if st.session_state.conv:
        chat_text = "\n\n".join(
            f"{msg['role'].upper()}: {msg['content']}"
            for msg in st.session_state.conv
        )
        st.download_button(
            label="📥 Download Conversation (.txt)",
            data=chat_text,
            file_name=f"{st.session_state.module}_chat_history.txt",
            mime="text/plain",
            help="Click to download your mentoring session as a text file",
        )

    # ------------------ ⬅️ Change Module ------------------
    if st.button("⬅️ Change Module"):
        st.session_state.module = None
        st.session_state.conv = []
        st.session_state.memory = []
        st.rerun()
