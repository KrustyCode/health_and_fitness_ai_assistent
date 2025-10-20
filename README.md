# 💪 Health & Fitness AI Assistant

An intelligent chatbot powered by RAG (Retrieval Augmented Generation) that provides evidence-based advice on fitness, nutrition, and exercise science. The system uses a pre-built knowledge base from professional fitness and nutrition documents.

## 🌟 Features

- **Expert Knowledge Base**: Answers based on professional fitness and nutrition literature
- **Conversational Interface**: Natural chat-based interaction
- **Fast Response**: Pre-embedded vector database for instant retrieval
- **Powered by LLaMA**: Uses Groq API with LLaMA 3.1 for intelligent responses

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key (get it free at [https://console.groq.com](https://console.groq.com))

## 🚀 Installation

### Option 1: Clone from GitHub

```bash
git clone https://github.com/KrustyCode/health_and_fitness_ai_assistent.git
cd health_and_fitness_ai_assistent
```

### Option 2: Manual Download

1. Download `app.py` (the main program)
2. Download the `faiss_index` folder (contains the pre-built vector database)
3. Place both in the same directory

## 📦 Install Dependencies

Run the following command in your terminal to install all required packages:

```bash
pip install PyMuPDF
pip install faiss-cpu
pip install langchain
pip install langchain-community
pip install langchain-core
pip install langchain-text-splitters
pip install sentence-transformers
pip install streamlit
pip install langchain-groq
```

## ▶️ Running the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## 🔑 Setup

1. When you first run the app, you'll be prompted to enter your **Groq API Key**
2. Get your free API key at: [https://console.groq.com](https://console.groq.com)
3. Paste your API key in the input field
4. Start asking questions!

## 💬 Usage Examples

Try asking questions like:

- "What is progressive overload in strength training?"
- "How much protein should I eat for muscle building?"
- "What are the best exercises for beginners?"
- "What should I eat before and after a workout?"

## 📁 Project Structure

```
health_and_fitness_ai_assistent/
├── app.py                    # Main Streamlit application
├── faiss_index/              # Pre-built vector database
│   ├── index.faiss          # FAISS vector index
│   └── index.pkl            # Document store
├── README.md                 # This file
```

## ⚙️ Technical Details

- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **LLM**: LLaMA 3.1 (8B Instant) via Groq API
- **Framework**: LangChain + Streamlit
- **Knowledge Base**: 10+ professional fitness and nutrition documents

## 🛠️ Troubleshooting

### "Vector database not found"
- Make sure the `faiss_index` folder is in the same directory as `app.py`
- Check that both `index.faiss` and `index.pkl` files exist inside the folder

### "Module not found" errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try reinstalling with `pip install --upgrade [package-name]`

### Slow first load
- The first time loading the embedding model may take 1-2 minutes
- Subsequent loads will be instant due to caching

## 📝 Notes

- The vector database contains pre-processed knowledge from fitness documents
- Original PDF files are NOT included - only the embedded text chunks
- Internet connection required for Groq API calls
- The embedding model downloads automatically on first run

## 🔗 Links

- GitHub Repository: [https://github.com/KrustyCode/health_and_fitness_ai_assistent](https://github.com/KrustyCode/health_and_fitness_ai_assistent)
- Groq API: [https://console.groq.com](https://console.groq.com)

---
