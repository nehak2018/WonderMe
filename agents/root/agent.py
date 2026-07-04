from google.adk.agents import SequentialAgent

from agents.story_agent.agent import root_agent as story_agent
from agents.safety_agent.agent import root_agent as safety_agent

root_agent = SequentialAgent(
    name="storybuddy_full_story_pipeline",
    description="Full Story Mode: story generation followed by child-safety review.",
    sub_agents=[
        story_agent,
        safety_agent,
    ],
)



