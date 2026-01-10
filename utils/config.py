import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    ZEP_API_KEY = os.getenv("ZEP_API_KEY")
    ZEP_API_URL = os.getenv("ZEP_API_URL")
    PHIDATA_API_KEY = os.getenv("PHIDATA_API_KEY")

    @classmethod
    def validate(cls):
        missing = []
        if not cls.GOOGLE_API_KEY:
            missing.append("GOOGLE_API_KEY")
        if not cls.ZEP_API_KEY:
            missing.append("ZEP_API_KEY")
        
        if missing:
            raise ValueError(f"Missing environment variables: {', '.join(missing)}")
