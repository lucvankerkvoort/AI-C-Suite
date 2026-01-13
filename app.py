import streamlit as st
import uuid
from agents.ceo import get_ceo_agent
from agents.cto import get_cto_agent
from utils.config import Config

# Brand Colors - Dark Mode
COLORS = {
    "navy": "#0E172A",
    "navy_deep": "#080D16",
    "slate": "#2A344B",
    "slate_light": "#3D4A63",
    "gold": "#C6A15B",
    "white": "#F8FAFC",
    "gray": "#6B7280",
    "gray_light": "#9CA3AF"
}

# Page configuration
st.set_page_config(
    page_title="Nexus | AI C-Suite",
    page_icon="🔹",
    layout="wide"
)

# Executive Dark CSS - Moody, High-Contrast, Enterprise-Grade
st.markdown(f"""
<style>
    /* Root variables */
    :root {{
        --navy: {COLORS['navy']};
        --navy-deep: {COLORS['navy_deep']};
        --slate: {COLORS['slate']};
        --slate-light: {COLORS['slate_light']};
        --gold: {COLORS['gold']};
        --white: {COLORS['white']};
        --gray: {COLORS['gray']};
        --gray-light: {COLORS['gray_light']};
    }}
    
    /* Main background - deep navy */
    .stApp {{
        background-color: var(--navy-deep);
    }}
    
    /* Main container */
    .main .block-container {{
        padding-top: 2rem;
        max-width: 900px;
    }}
    
    /* All text white by default */
    .stApp, .stApp p, .stApp span, .stApp label {{
        color: var(--white);
    }}
    
    /* Sidebar - slightly lighter navy */
    section[data-testid="stSidebar"] {{
        background-color: var(--navy);
        border-right: 1px solid var(--slate);
    }}
    
    section[data-testid="stSidebar"] * {{
        color: var(--white) !important;
    }}
    
    section[data-testid="stSidebar"] .stCaption {{
        color: var(--gray) !important;
    }}
    
    /* Agent card styling */
    .agent-card {{
        background: var(--slate);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 3px solid var(--gold);
    }}
    
    .agent-card h3 {{
        margin: 0 0 0.5rem 0;
        color: var(--white);
        font-weight: 500;
    }}
    
    .agent-card p {{
        margin: 0;
        color: var(--gray-light);
        font-size: 0.85rem;
    }}
    
    /* Chat messages - dark cards */
    .stChatMessage {{
        background: var(--slate) !important;
        border: 1px solid var(--slate-light);
        border-radius: 8px;
    }}
    
    .stChatMessage * {{
        color: var(--white) !important;
    }}
    
    /* Welcome container */
    .welcome-container {{
        text-align: center;
        padding: 3rem 2rem;
        background: var(--navy);
        border-radius: 8px;
        border: 1px solid var(--slate);
        margin: 2rem 0;
    }}
    
    .welcome-container h2 {{
        color: var(--white);
        margin-bottom: 0.5rem;
        font-weight: 500;
    }}
    
    .welcome-container p {{
        color: var(--gray-light);
    }}
    
    /* Buttons */
    .stButton > button {{
        background: var(--slate);
        color: var(--white);
        border: 1px solid var(--slate-light);
        border-radius: 6px;
        font-weight: 500;
    }}
    
    .stButton > button:hover {{
        background: var(--slate-light);
        border-color: var(--gold);
        color: var(--white);
    }}
    
    /* Chat input */
    .stChatInput {{
        background: var(--navy) !important;
    }}
    
    .stChatInput textarea {{
        background: var(--slate) !important;
        color: var(--white) !important;
        border: 1px solid var(--slate-light) !important;
    }}
    
    .stChatInput textarea::placeholder {{
        color: var(--gray) !important;
    }}
    
    /* Radio buttons in sidebar - compact */
    section[data-testid="stSidebar"] .stRadio label {{
        background: var(--slate);
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        margin-bottom: 0.25rem;
        display: block;
        border: 1px solid transparent;
        font-size: 0.9rem;
    }}
    
    section[data-testid="stSidebar"] .stRadio label:hover {{
        background: var(--slate-light);
    }}
    
    section[data-testid="stSidebar"] .stRadio > div {{
        gap: 0.25rem;
    }}
    
    /* Dividers - subtle gold */
    hr {{
        border-color: var(--gold);
        opacity: 0.2;
    }}
    
    /* Headers */
    h1, h2, h3, h4 {{
        color: var(--white);
        font-weight: 500;
    }}
    
    /* Gold accents */
    .gold-accent {{
        color: var(--gold);
    }}
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: var(--navy-deep);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: var(--slate);
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: var(--slate-light);
    }}
    
    /* Hide Streamlit branding but keep header for sidebar toggle */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# Agent definitions
AGENTS = {
    "CEO": {
        "icon": "🔹",
        "title": "Chief Executive Officer",
        "description": "Strategic direction & high-level decisions"
    },
    "CTO": {
        "icon": "🔹",
        "title": "Chief Technology Officer", 
        "description": "Technical architecture & code scaffolding"
    },
    "CMO": {
        "icon": "🔹",
        "title": "Chief Marketing Officer",
        "description": "Marketing strategy & growth"
    }
}

# Session ID for memory persistence
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Sidebar
with st.sidebar:
    st.markdown("## 🔹 NEXUS")
    st.caption("Executive AI Suite")
    
    st.divider()
    
    # API Key check
    if not Config.GOOGLE_API_KEY:
        st.error("Missing API Key")
        st.caption("Add GOOGLE_API_KEY to .env")
    
    # Agent selection
    st.caption("SELECT AGENT")
    selected_agent = st.radio(
        "agent",
        list(AGENTS.keys()),
        format_func=lambda x: f"{x}",
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Session controls
    if st.button("New Session", use_container_width=True):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()
    
    st.caption(f"Session: {st.session_state.session_id[:8]}")

# Main chat area
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome screen when no messages
if not st.session_state.messages:
    st.markdown(f"""
    <div class="welcome-container">
        <h2>Welcome to Nexus</h2>
        <p>Your AI {AGENTS[selected_agent]['title']} is ready</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Prompt suggestions
    st.markdown("#### Suggested prompts")
    
    suggestions = {
        "CEO": [
            "What should our Q1 priorities be?",
            "How do we evaluate product-market fit?",
            "Draft a vision statement"
        ],
        "CTO": [
            "Scaffold a FastAPI project",
            "What tech stack for a SaaS MVP?",
            "Create a basic project structure"
        ],
        "CMO": [
            "Draft a launch announcement",
            "What channels for B2B marketing?",
            "Create a content calendar"
        ]
    }
    
    cols = st.columns(3)
    for i, suggestion in enumerate(suggestions[selected_agent]):
        with cols[i]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": suggestion})
                st.rerun()

# Display chat history
for message in st.session_state.messages:
    avatar = "🔹" if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input(f"Message {selected_agent}..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent
    agent = None
    if selected_agent == "CEO":
        agent = get_ceo_agent(session_id=st.session_state.session_id)
    elif selected_agent == "CTO":
        agent = get_cto_agent(session_id=st.session_state.session_id)
    
    if agent:
        with st.chat_message("assistant", avatar="🔹"):
            with st.spinner(""):
                try:
                    response = agent.run(prompt)
                    response_text = response.content
                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.info(f"{selected_agent} agent coming soon")
