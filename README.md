# Terminal 1 - Run Ollama LLM
ollama run llama2

# Terminal 2 - Start FastAPI
cd backend
uvicorn main:app --reload

# Terminal 3 - Start Streamlit frontend
cd frontend
streamlit run app.py
