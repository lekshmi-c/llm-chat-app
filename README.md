# Local LLM Chat Application

A lightweight, **100% locally-run** chat application that lets you interact with open-source large language models (LLMs) like **Llama 2**, **Mistral**, or **Gemma**—all on your own machine. Built with **Streamlit** (frontend), **FastAPI** (backend), and **Ollama** (LLM runtime), this project ensures **privacy**, **offline capability**, and **no cloud dependencies**.

---

## ✨ Key Features

- **Fully Local**: No internet, API keys, or external services required.
- **Model Flexibility**: Easily switch between any model supported by Ollama (e.g., `llama2`, `mistral`, `gemma`).
- **Simple & Clean UI**: Intuitive chat interface powered by Streamlit.
- **Modular Architecture**: Decoupled frontend (Streamlit) and backend (FastAPI) for easy customization.

---

## 🛠️ Prerequisites

- **Python 3.8–3.11**  
  > ⚠️ Note: Streamlit may have compatibility issues with Python 3.12+. Use Python 3.11 if you encounter installation errors.
- **Ollama** – [Download and install from ollama.ai](https://ollama.ai/)
- **Pip** – Python package manager

---

## 🚀 Quick Start

### 1. Install Ollama and a Model
```bash
# Install Ollama from https://ollama.ai/
# Then pull your preferred model:
ollama pull llama2
# Or: ollama pull mistral, gemma, etc.
```

### 2. Clone the Repository
```bash
git clone https://github.com/lekshmi-c/llm-chat-app.git
cd llm-chat-app
```

### 3. Set Up Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
# Backend (FastAPI)
cd backend
pip install -r requirements.txt

# Frontend (Streamlit)
cd ../frontend
pip install -r requirements.txt
```

### 5. Run the Application

> Open **two separate terminal windows**.

**Terminal 1 – Start Backend (FastAPI):**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**Terminal 2 – Start Frontend (Streamlit):**
```bash
cd frontend
streamlit run app.py
```

- **Backend API**: http://localhost:8000  
- **Chat Interface**: http://localhost:8501

> 🔔 **Important**: Do **not** run `python main.py` for the backend. FastAPI apps must be launched with `uvicorn`.

---

## 🗂️ Project Structure

```
llm-chat-app/
├── backend/
│   ├── main.py           # FastAPI server (interfaces with Ollama)
│   └── requirements.txt  # FastAPI, uvicorn, etc.
├── frontend/
│   ├── app.py            # Streamlit UI
│   └── requirements.txt  # Streamlit, requests
├── .venv/                # Virtual environment (optional)
└── README.md             # This file
```

---

## 🎨 Customization

### Change Default Model
Edit `frontend/app.py`:
```python
st.session_state.selected_model = "mistral"  # or "llama2", "gemma", etc.
```

### Update UI Title & Icon
In `frontend/app.py`:
```python
st.set_page_config(page_title="My AI Assistant", page_icon="✨")
```

### Adjust Backend Timeout
In `backend/main.py`, modify the subprocess timeout:
```python
result = subprocess.run(..., timeout=60)  # Increase if needed
```

### List Available Models via API
Send a GET request to:
```
GET http://localhost:8000/api/models
```

---

## ⚠️ Known Issues

- **Streamlit + Python 3.12+**: May fail to install or run. **Workaround**: Use Python 3.11.
- **Running FastAPI**: Always use `uvicorn main:app`, **not** `python main.py`.

---

## 📄 License

This project is open-source. See the repository for license details.

---

> 💡 **Tip**: Experiment with different Ollama models by simply changing the model name—no code changes needed beyond the default setting!
