from google.adk.agents import LlmAgent
from .story_skills import get_story_rules

root_agent = LlmAgent(
    name="story_agent",
    model="gemini-2.5-flash",
    description="Creates short, age-appropriate children's stories.",
    instruction=get_story_rules()
)