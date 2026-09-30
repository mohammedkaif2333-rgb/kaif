import streamlit as st
from openai import OpenAI
import os

# Set page configuration
st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.markdown("A simple web-based AI assistant using Streamlit and OpenAI.")

# Get API key from environment variable or user input
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.warning("OPENAI_API_KEY environment variable not found. You can enter it below for this session.")
    api_key = st.text_input("OpenAI API Key", type="password")

if not api_key:
    st.info("Please provide your OpenAI API key to start chatting.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Display chat messages from history on app rerun (skipping system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )

            assistant_response = response.choices[0].message.content
            message_placeholder.markdown(assistant_response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        st.error(f"An error occurred: {e}")
