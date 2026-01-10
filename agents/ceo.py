from phi.agent import Agent
from phi.model.google import Gemini
from utils.config import Config

# Initialize configuration to ensure API keys are present
try:
    Config.validate()
except ValueError:
    pass # Allow import even if config is missing, for scaffolding purposes

def get_ceo_agent():
    return Agent(
        name="CEO",
        role="Chief Executive Officer",
        model=Gemini(id="gemini-1.5-pro", api_key=Config.GOOGLE_API_KEY),
        instructions=[
            "You are the CEO of a tech startup.",
            "Your goal is to provide high-level strategic direction.",
            "You delegate tasks to your CTO and CMO."
        ],
        show_tool_calls=True,
        markdown=True,
    )
