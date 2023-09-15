import openai
import streamlit as st

# Load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧑‍💻 Data-Espresso 💬 Chatbot")
"""
My name is Data-barista ☕️ . 
I know many things, ask me anything you like, 
but please. Dont ask me stupid questions❓
"""
if "messages" not in st.session_state:
    st.session_state["messages"] = [
    {"role": "system", "content": "You are a sacarstic assistant called Data-Barista, you love to use emojis."}
    ]
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)