# hello_streamlit.py
# Example from https://tingyuansen.github.io/coding_essential_for_astronomers/lectures/lecture10-streamlit.html 
# Links to an external site.

# simple_chat.py
import streamlit as st

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    # Validate that messages are dictionaries, reset if corrupted
    if st.session_state.messages and not isinstance(st.session_state.messages[0], dict):
        st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    # Ensure msg is a dictionary with required keys
    if isinstance(msg, dict) and "role" in msg and "content" in msg:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Handle input
if prompt := st.chat_input("Type here"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add response
    response = f"Echo: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)