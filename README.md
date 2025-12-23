# AI_Chatbot_Mentor
# 🤖 AI Chatbot Mentor – Domain-Specific Intelligent Learning Assistant

AI Chatbot Mentor is an interactive, AI-powered mentoring application designed to provide **focused, domain-specific learning guidance** across multiple technical modules.

Unlike generic chatbots, this system strictly answers questions **only within the selected module**, ensuring accurate, relevant, and distraction-free mentorship.

---

## 📌 Project Overview

The goal of this project is to demonstrate how **domain-restricted AI systems** can be built for real-world educational use cases.

The application uses **Streamlit** for the user interface and **LangChain** for orchestrating LLM interactions, prompt control, and conversation memory.

---

## 🎯 Key Features

* ✅ Module-based AI mentoring
* ✅ Strict domain restriction (no out-of-scope answers)
* ✅ Rejection of irrelevant questions
* ✅ Session-based conversation memory
* ✅ Downloadable chat history (.txt)
* ✅ Clean and user-friendly Streamlit UI

---

## 📚 Available Learning Modules

* Python
* SQL
* Power BI
* Exploratory Data Analysis (EDA)
* Machine Learning (ML)
* Deep Learning (DL)
* Generative AI (Gen AI)
* Agentic AI

---

## 🧠 Application Flow

1. **Welcome Screen**
   Displays a greeting message and prompts the user to select a learning module.

2. **Module Selection**
   User selects one module from the available list.

3. **Module-Specific Mentor Interface**
   A dedicated AI mentor is activated for the selected module.

4. **Question Handling Logic**

   * Relevant questions → answered clearly and educationally
   * Irrelevant questions → rejected with a fixed response:

   > *"Sorry, I don’t know about this question. Please ask something related to the selected module."*

5. **Conversation Memory**
   Full chat history is maintained during the session.

6. **Download Conversation**
   User can download the entire conversation in `.txt` format anytime.

---

## 🛠 Tech Stack

| Component        | Technology                             |
| ---------------- | -------------------------------------- |
| Frontend         | Streamlit                              |
| AI Orchestration | LangChain                              |
| LLM              | Open-source / API-based (Configurable) |
| Memory           | LangChain Conversation Memory          |
| Export           | Text (.txt)                            |

---

## ⚙️ Functional Requirements

* Module-based AI mentoring system
* Strict domain enforcement
* Conversation history persistence (session-based)
* Chat history download functionality
* Simple and clean UI

---

## 📂 Suggested Project Structure

```
AI-Chatbot-Mentor/
│
├── app.py                  # Main Streamlit application
├── prompts/
│   ├── python_prompt.py
│   ├── sql_prompt.py
│   ├── ml_prompt.py
│   └── ...
├── utils/
│   ├── memory.py           # Conversation memory handling
│   ├── validator.py        # Domain validation logic
│   └── exporter.py         # Chat export (.txt)
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/your-username/AI-Chatbot-Mentor.git
cd AI-Chatbot-Mentor
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📥 Download Chat History Feature (Highlight)

* Entire conversation (user + AI responses)
* Downloadable as `.txt`
* Useful for:

  * Revision
  * Notes
  * Portfolio documentation
  * Offline learning

---

## 🎓 Learning Outcomes

By completing this project, you will learn:

* How to build domain-restricted AI chatbots
* Prompt engineering for controlled AI responses
* Using LangChain with conversation memory
* Designing interactive applications with Streamlit
* Implementing chat export functionality
* Structuring real-world AI mentor systems

---

## 🏁 Conclusion

AI Chatbot Mentor demonstrates how intelligent systems can be designed to deliver **focused, reliable, and learner-centric AI mentorship**.

It bridges the gap between generic chatbots and real-world educational AI assistants by enforcing strict domain control and offering practical usability features like conversation download.

---

## 🙏 Acknowledgements

* **Innomatics Research Labs** – for structured learning and guidance
* **Saxon K Sha** – for mentorship inspiration

---

## 📌 License

This project is intended for educational and learning purposes.
