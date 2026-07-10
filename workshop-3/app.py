import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="Mini ChatGPT - Mistral",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mini ChatGPT (Mistral AI)")


api_key = "dLXkFze2LRfFnT1O8iVBmSyE4OOBx6li"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:

    if not api_key:
        st.error("Please enter your API key.")
        st.stop()

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.mistral.ai/v1"
    )

  
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    try:
        response = client.chat.completions.create(
            model="mistral-small-latest",
            messages=st.session_state.messages
        )

        assistant_reply = response.choices[0].message.content

    
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply}
        )

    except Exception as e:
        st.error(f"Error: {e}")
