from zep_python import ZepClient
from utils.config import Config

class MemoryClient:
    _instance = None

    @classmethod
    def get_client(cls):
        if cls._instance is None:
            Config.validate()
            cls._instance = ZepClient(
                api_key=Config.ZEP_API_KEY,
                base_url=Config.ZEP_API_URL
            )
        return cls._instance

    @staticmethod
    def add_memory(session_id, role, content):
        client = MemoryClient.get_client()
        # Zep implementation details would go here
        # This is a scaffold, so we'll keep it simple for now
        pass

    @staticmethod
    def get_memory(session_id):
        client = MemoryClient.get_client()
        # Retrieve memory logic
        return []
