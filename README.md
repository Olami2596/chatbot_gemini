# Gemini Chatbot

A simple and interactive chatbot web application built with **Streamlit** and powered by **Google's Gemini AI model**. This app allows users to have conversations with an AI assistant.

## Features

- **Interactive Chat Interface**  
  Engage in a conversational chat with the Gemini AI model through a user-friendly web interface.

- **Clear Chat History**  
  Reset the conversation with a single button click to start fresh.

- **Markdown Formatting**  
  Assistant responses are formatted using Markdown for improved readability (e.g., **bold**, *italics*, lists).

- **Loading Indicator**  
  Displays a "Gemini is thinking..." spinner while waiting for AI responses, enhancing user experience.

- **Error Handling**  
  Gracefully handles API errors (e.g., invalid API key, network issues) with user-friendly messages.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.8+**: Required to run the app.
- **Google Gemini API Key**: Obtain from Google and store in a `.env` file.
- **Required Libraries**: Install using the provided `requirements.txt`.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
````

### 2. Set Up a Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

* Create a `.env` file in the project root directory.
* Add your Gemini API key:

```
GEMINI_API_KEY='your-api-key-here'
```

> Replace `your-api-key-here` with your actual Gemini API key.

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run Gemini_Chatbot_Enhanced.py
```

The app will open in your default web browser (typically at `http://localhost:8501`).

---

## Usage

* **Chat with the Assistant**
  Type your message in the "Ask Gemini..." input box and press Enter.
  The assistant responds with Markdown-formatted text (e.g., **bold**, *italics*, or `-` lists).
  A "Gemini is thinking..." spinner appears while waiting for the response.

* **Clear Chat History**
  Click the **"Clear Chat History"** button to reset the conversation.

* **Handle Errors**
  If an error occurs (e.g., invalid API key or network issue), a user-friendly message appears in the chat and as a red alert.

---

## Dependencies

The `requirements.txt` file includes:

* `streamlit`
* `google-genai`

Install them with:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

* **Invalid API Key**:
  Ensure your `GEMINI_API_KEY` is correctly set in the `.env` file.

* **Network Issues**:
  Check your internet connection if you encounter a network error.

* **Library Errors**:
  Ensure all dependencies are installed properly using `pip install -r requirements.txt`.

* **Gemini API Errors**:
  If the API returns an error (e.g., rate limits), wait and try again or refer to the Gemini API documentation.

---

