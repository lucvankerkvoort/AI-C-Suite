from phi.storage.agent.sqlite import SqlAgentStorage
import os

# Ensure data directory exists
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_FILE = os.path.join(DATA_DIR, "nexus.db")

def get_agent_storage(table_name: str = "agent_sessions") -> SqlAgentStorage:
    """
    Returns a SQLite storage instance for agent memory.
    
    Args:
        table_name: Name of the table to store sessions in.
                   Use different names for different agents if needed.
    
    Returns:
        SqlAgentStorage instance configured for local SQLite.
    """
    return SqlAgentStorage(
        table_name=table_name,
        db_file=DB_FILE
    )
