import streamlit as st
from openai import OpenAI

# =========================================
# Page Configuration
st.set_page_config(
    page_title="Mini ChatGPT - Mistral",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mini ChatGPT (Mistral AI)")

# Your Mistral API Key
api_key = "dLXkFze2LRfFnT1O8iVBmSyE4OOBx6li"

# =========================================
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# =========================================
# Display previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# =========================================
# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:

    if not api_key:
        st.error("Please enter your API key.")
        st.stop()

    # Create Mistral client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.mistral.ai/v1"
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Generate assistant response
    try:
        response = client.chat.completions.create(
            model="mistral-small-latest",
            messages=st.session_state.messages
        )

        assistant_reply = response.choices[0].message.content

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        # Save assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply}
        )

    except Exception as e:
        st.error(f"Error: {e}")
