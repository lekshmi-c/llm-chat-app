import streamlit as st
import requests
import time

# Configuration
BACKEND_URL = "http://localhost:8000"  # Change if backend is hosted elsewhere
# BACKEND_URL = "http://backend:8000"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "llama2"

# Fetch available models
# @st.cache_data(ttl=60)
# def get_models():
#     try:
#         response = requests.get(f"{BACKEND_URL}/api/models")
#         if response.status_code == 200:
#             return response.json().get("models", ["llama2"])
#         return ["llama2"]
#     except:
#         return ["llama2"]

# Function to get chat response
def get_chat_response(prompt):
    messages = [{"role": msg["role"], "content": msg["content"]} 
               for msg in st.session_state.messages]
    
    data = {
        "model": st.session_state.selected_model,
        "messages": messages,
        "stream": False
    }
    
    response = requests.post(f"{BACKEND_URL}/api/chat", json=data)
    if response.status_code == 200:
        return response.json().get("response", "No response")
    return f"Error: {response.text}"

# Streamlit UI
st.title("Local LLM Chat App")

# Model selection
st.session_state.selected_model = "llama2"
# available_models = get_models()
# st.session_state.selected_model = st.selectbox(
#     "Select Model",
#     available_models,
#     index=available_models.index(st.session_state.selected_model) if st.session_state.selected_model in available_models else 0
# )

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate streaming for better UX
        with st.spinner("Thinking..."):
            assistant_response = get_chat_response(prompt)
            
            # Simulate character-by-character display
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})