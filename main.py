import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai-key"])

st.title("Chatbot")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt the user for input
if prompt := st.chat_input("Hello, how can I help you?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    conversation = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]


    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            response = client.chat.completions.create(model=st.session_state["openai_model"],
            messages=conversation)
            # Extract and display the assistant's response
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
