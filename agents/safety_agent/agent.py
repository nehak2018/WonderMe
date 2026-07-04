from google.adk.agents import LlmAgent
from .safety_skills import get_safety_rules

root_agent = LlmAgent(
    name="safety_agent",
    model="gemini-2.5-flash",
    description="Reviews children's stories for safety.",
    instruction=get_safety_rules()
)
