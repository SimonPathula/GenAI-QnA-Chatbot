# 🤖 QnA Chatbot

A conversational Q&A chatbot built with **LangChain**, **Ollama**, and **Streamlit**. Ask any question and get AI-powered responses — all running locally using open-source LLMs via Ollama.

---

## ✨ Features

- 💬 Interactive chat interface powered by **Streamlit**
- 🧠 Supports multiple local AI models via **Ollama** (Gemma, LLaMA, Qwen)
- 🔗 Built with **LangChain** for seamless LLM chaining
- 🎛️ Adjustable **Temperature** and **Max Tokens** via sidebar
- 🔍 LangSmith tracing integration for observability
- 🔐 Environment-based API key management with `python-dotenv`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [LangChain](https://www.langchain.com/) | LLM orchestration |
| [Ollama](https://ollama.com/) | Local LLM inference |
| [LangSmith](https://smith.langchain.com/) | Tracing & observability |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
QnA Chatbot/
│
├── app.py              # Main Streamlit app
├── main.py             # Entry point
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running locally

### 1. Clone the Repository

```bash
git clone https://github.com/SimonPathula/QnA-Chatbot.git
cd QnA-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

> 🔑 Get your LangSmith API key at [smith.langchain.com](https://smith.langchain.com/)

### 5. Pull Ollama Models

Make sure Ollama is running and pull the models you want to use:

```bash
ollama pull gemma:2b
ollama pull llama3.2:3b
ollama pull qwen:2b
```

### 6. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🎮 Usage

1. Open the app in your browser
2. Use the **sidebar** to:
   - Select an AI model (`gemma:2b`, `llama:3b`, or `qwen:2b`)
   - Adjust **Temperature** (controls creativity, 0.0–1.0)
   - Adjust **Max Tokens** (controls response length, 50–300)
3. Type your question in the input box and press Enter
4. The chatbot will respond instantly!

---

## 📦 Dependencies

```
langchain
langchain_core
langchain_community
langchain_openai
langchain_groq
langchain_ollama
streamlit
python-dotenv
```

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `LANGCHAIN_API_KEY` | Your LangSmith API key for tracing |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Simon Pathula**  
GitHub: [@SimonPathula](https://github.com/SimonPathula)