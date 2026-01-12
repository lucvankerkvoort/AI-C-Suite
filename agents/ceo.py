from phi.agent import Agent
from phi.model.google import Gemini
from utils.config import Config
from memory.storage import get_agent_storage

def get_ceo_agent(session_id: str = None):
    """
    Returns a CEO agent configured with Gemini and SQLite storage.
    
    Args:
        session_id: Optional session ID for conversation continuity.
    """
    return Agent(
        name="CEO",
        role="Chief Executive Officer",
        model=Gemini(id="gemini-2.5-pro", api_key=Config.GOOGLE_API_KEY),
        storage=get_agent_storage("ceo_sessions"),
        session_id=session_id,
        instructions=[
            "You are the CEO of a tech startup.",
            "Your goal is to provide high-level strategic direction.",
            "You delegate tasks to your CTO and CMO."
        ],
        add_history_to_messages=True,
        num_history_responses=10,
        show_tool_calls=True,
        markdown=True,
    )
