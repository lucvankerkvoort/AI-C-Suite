from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.file import FileTools
from utils.config import Config
from memory.storage import get_agent_storage
import os

# Workspace directory for CTO file operations
WORKSPACE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workspace")
os.makedirs(WORKSPACE_DIR, exist_ok=True)

def get_cto_agent(session_id: str = None):
    """
    Returns a CTO agent configured with Gemini and FileTools.
    
    The CTO can read, write, and list files in the ./workspace directory.
    
    Args:
        session_id: Optional session ID for conversation continuity.
    """
    return Agent(
        name="CTO",
        role="Chief Technology Officer",
        model=Gemini(id="gemini-1.5-pro", api_key=Config.GOOGLE_API_KEY),
        storage=get_agent_storage("cto_sessions"),
        session_id=session_id,
        tools=[
            FileTools(
                base_dir=WORKSPACE_DIR,
                save_files=True,
                read_files=True,
                list_files=True
            )
        ],
        instructions=[
            "You are the CTO of a tech startup.",
            "You help scaffold code projects and write files to the workspace.",
            "When asked to create files or scaffold projects, use your file tools to actually create the files.",
            "Always confirm what files you created and their locations.",
            "For scaffolding requests, create a proper directory structure with all necessary files.",
            f"All files are saved to: {WORKSPACE_DIR}"
        ],
        add_history_to_messages=True,
        num_history_responses=10,
        show_tool_calls=True,
        markdown=True,
    )
