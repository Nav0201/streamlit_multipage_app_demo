import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Connect with me on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hi! What's up? Feel free to check out my LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hello! Need assistance? Let's connect on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hey! Got a question? Reach out to me on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hi there! How can I help? Connect with me here: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hello! Looking for help? Let's connect on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hey! Need assistance? Find me on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hi! Got any questions? Connect with me on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hello! Need help? Let’s network on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
            "Hey there! Any questions? Let's connect on LinkedIn: https://www.linkedin.com/in/naveen-a-9101001b6/",
        ]
    )

    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
