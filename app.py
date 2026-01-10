import streamlit as st
import uuid
from agents.ceo import get_ceo_agent
from utils.config import Config

st.set_page_config(page_title="AI C-Suite", page_icon="👔")

st.title("AI C-Suite 👔")

# Session ID for memory persistence
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    if not Config.GOOGLE_API_KEY:
        st.warning("Google API Key not found. Please set it in .env")
    
    selected_agent = st.selectbox("Select Agent", ["CEO", "CTO", "CMO"])
    
    st.divider()
    st.caption(f"Session: {st.session_state.session_id[:8]}...")
    if st.button("New Session"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

# Main Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask the C-Suite..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent Response
    if selected_agent == "CEO":
        try:
            agent = get_ceo_agent(session_id=st.session_state.session_id)
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                response = agent.run(prompt)
                response_text = response.content
                response_placeholder.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"Error communicating with agent: {e}")
    else:
        st.info(f"{selected_agent} agent is not yet implemented.")
