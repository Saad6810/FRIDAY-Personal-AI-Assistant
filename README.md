# FRIDAY: Personal AI Assistant

FRIDAY is a personal AI assistant backend built with FastAPI. It combines a
Groq-hosted LLM with Retrieval-Augmented Generation (RAG) over your own
documents and optional live web search, so it can answer from your personal
knowledge base and from current information on the internet.

## Features

- Two chat modes:
  - General: LLM + your own documents (FAISS vector store), no web search
  - Realtime: LLM + your documents + live web results via Tavily
- RAG with sentence-transformer embeddings and a FAISS index
- Persistent chat sessions saved as JSON, shared across both modes
- Multiple Groq API keys with round-robin rotation and automatic fallback on rate limits
- Configurable assistant name and personality through environment variables
- REST API with auto-generated docs at /docs, plus a command-line client

## Tech Stack

Python, FastAPI, Uvicorn, Pydantic, LangChain, Groq, FAISS,
Hugging Face sentence-transformers, Tavily, python-dotenv

## API Keys Required

This project needs your own API keys. No keys are included in this repository.

| Service | Required? | What it's for | Get a key |
|---|---|---|---|
| Groq | Yes | Runs the LLM. The server won't start without it. | https://console.groq.com |
| Tavily | Optional | Live web search in Realtime mode. Without it, Realtime mode has no web results. | https://tavily.com |

Both services offer a free tier that is enough for personal use.

## Getting Started

1. Clone the repo:

```bash
git clone https://github.com/Saad6810/FRIDAY-Personal-AI-Assistant.git
cd FRIDAY-Personal-AI-Assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a file named `.env` in the project root and add your keys:

```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
ASSISTANT_NAME=Friday
```

Optional settings:
- `GROQ_API_KEY_2`, `GROQ_API_KEY_3`, ... : extra Groq keys. The server rotates
  through them and falls back to the next one if a key hits its rate limit.
- `FRIDAY_USER_TITLE`: how the assistant should address you (for example "Sir").

4. (Optional) Add `.txt` files with information about yourself to
   `database/learning_data/`. The assistant retrieves relevant parts of them
   when answering.

5. Start the server:

```bash
python run.py
```

The first start downloads the embedding model, so it may take a minute.
Wait for "Friday is online and ready!".

6. In a second terminal, start the chat client:

```bash
python test.py
```

Type `1` for General mode or `2` for Realtime mode, then start chatting.

## Security

- Never commit your `.env` file. It is listed in `.gitignore`.
- If you accidentally publish a key, delete it on the provider's dashboard and
  create a new one immediately.
- Chat history is stored locally in `database/chats_data/` and is not uploaded.

## API Endpoints

| Endpoint | Description |
|---|---|
| POST /chat | General chat (no web search) |
| POST /chat/realtime | Realtime chat (with web search) |
| GET /chat/history/{session_id} | Retrieve a session's history |
| GET /health | Service health check |

Interactive API docs are available at http://localhost:8000/docs while the
server is running.
