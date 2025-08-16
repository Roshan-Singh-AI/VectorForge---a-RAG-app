"""Streamlit app main file."""

import streamlit as st

from src.config import groq_llm_model

st.set_page_config(
    page_title="VectorForge"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

def main():
    """Initialize and render the Streamlit app interface."""

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": "prompt"})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Waiting For Response..."):
                response = st.write_stream(
                    groq_llm_model.stream(prompt)
                )

        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()