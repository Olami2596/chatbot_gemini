import os
from dotenv import load_dotenv
import streamlit as st
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Set the title and icon of the Streamlit app
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered",
)

# Set page title
st.title("Gemini Chatbot 🤖")

# Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()

# Initialize chat session in Streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Prepare the message history for Gemini
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant. Format your responses using Markdown for clarity (e.g., use **bold**, *italics*, or - lists)."})
    messages.extend(st.session_state.chat_history)
    contents = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])

    # Call Gemini API with improved error handling
    try:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
            )
        assistant_response = response.text
    except genai.AuthenticationError:
        assistant_response = "**Error**: Invalid API key. Please check your GEMINI_API_KEY in the .env file."
        st.error(assistant_response)
    except genai.APIError as e:
        assistant_response = f"**Error**: The Gemini API encountered an issue. Please try again later. (Details: {str(e)})"
        st.error(assistant_response)
    except ConnectionError:
        assistant_response = "**Error**: Network issue. Please check your internet connection and try again."
        st.error(assistant_response)
    except Exception as e:
        assistant_response = f"**Error**: An unexpected issue occurred. Please try again or contact support. (Details: {str(e)})"
        st.error(assistant_response)

    # Store and display assistant's response
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)