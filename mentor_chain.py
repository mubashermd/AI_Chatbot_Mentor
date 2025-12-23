import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

def load_prompt(module_name: str) -> str:
    """Load the prompt template file for a given module."""
    file_name = module_name.lower().replace(" ", "_") + ".txt"
    file_path = os.path.join("prompts", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def create_gemini_chain(module_name: str):
    """Create a LangChain conversation chain using Gemini 2.5 Flash."""
    prompt_template = load_prompt(module_name)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # use Gemini 2.5 Flash model
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=prompt_template
    )

    memory = ConversationBufferMemory(return_messages=True)
    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )
    return chain
