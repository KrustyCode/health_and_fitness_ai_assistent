import streamlit as st
import os
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


## This is the main script for running the Customized Chatbot.
## The chatbot is designed to have knowledge as a nutrition and fitness instructor.
## You can use it for various consultations, such as creating exercise schedules, calculating your nutritional intake, or even asking for healthy and delicious recipes.

## Instructions:
## - Install all dependencies before running the program.
## - Make sure you have a folder named "faiss_index" in the same directory as this file.
## - The "faiss_index" folder should contain both "index.faiss" and "index.pkl".
## - Run the code using: 'streamlit run app.py'


st.title("💪 Fitness & Nutrition AI Assistant")

PROMPT_TEMPLATE = """
Your name is Husor (Humble Instructor)
You are a knowledgeable, humble, and supportive nutrition and fitness instructor. 
Your role is to guide the user with clear, accurate, and encouraging explanations based on reliable information.

Use the provided context below to answer the user’s question. 
If the answer cannot be found in the context, politely say you don’t know and suggest what the user could do next (e.g., consult a professional or seek reliable sources).

Keep your response concise, supportive, and easy to understand, aim for clarity and motivation, not technical jargon.
"""

# Set role fore each massage type
MESSAGE_ROLE = {
    HumanMessage: "User",
    AIMessage: "Assistant",
}

# Loaded once
@st.cache_resource
def load_vector_db(model_name: str):
    """
    """
    if not os.path.exists("faiss_index"):
        st.error("Vector database not found.")
        st.stop()
    
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vector_db = FAISS.load_local(
        "faiss_index", 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    return vector_db


def display_one_message(message):
    """
    Display a single chat message in the Streamlit interface
    according to its message type (User or Assistant).
    """
    role = MESSAGE_ROLE[type(message)]
    with st.chat_message(role):
        st.markdown(message.content)

# Request an API key from the user if none is stored in the current session
if "groq_api_key" not in st.session_state or not st.session_state["groq_api_key"]:
    api_key = st.text_input("🔑 Enter your Groq AI API Key", type="password")
    if api_key:
        st.session_state["groq_api_key"] = api_key
        st.rerun()
    else:
        st.stop()

# Initialize the LLM model for the current session
if "llm" not in st.session_state:
    st.session_state["llm"] = ChatGroq(
        model="llama-3.1-8b-instant", groq_api_key=st.session_state["groq_api_key"]
    )

llm = st.session_state["llm"]

# Load the vector database for document retrieval
vector_db = load_vector_db("sentence-transformers/all-MiniLM-L6-v2")

# Initialize the chat history for the current session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
chat_history = st.session_state["chat_history"]

# Display all messages stored in the chat history
for msg in chat_history:
    display_one_message(msg)

# Streamlit input field for the user to enter their message
user_prompt = st.chat_input("Type your message here...")

# Stop execution if no user input is provided
if not user_prompt:
    st.stop()

# Retrieve the most relevant documents from the vector database based on the user query
relevant_docs = vector_db.similarity_search(user_prompt, k=3)

# Combine the retrieved documents into a single context string
docs_content = "\n\n".join(doc.page_content for doc in relevant_docs)

# Construct the structured message for the AI
# The message consists of: system prompt (AI behavior setup) and human message (user query)
prompt = chat_history.copy()
prompt.append(SystemMessage(content=PROMPT_TEMPLATE))
prompt.append(HumanMessage(content=f"Context: {docs_content}\n\nQuestion: {user_prompt}"))

# Display the user's message
chat_history.append(HumanMessage(content=user_prompt))
display_one_message(chat_history[-1])

# Send the prompt to the AI model and receive a response
response = llm.invoke(prompt)

# Add the AI's response to the chat history and display it
chat_history.append(response)
display_one_message(chat_history[-1])
