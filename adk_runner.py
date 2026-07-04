import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv
import os


APP_NAME = "WonderMe_app"
USER_ID = "user"


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    print("API Key loaded:", api_key[:10])
else:
    print("NO API KEY FOUND")


async def run_agent_async(agent, prompt: str, session_id: str = "default"):
    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )

    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    content = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )

    final_text = ""

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    final_text = part.text

    return final_text


def run_agent(agent, prompt: str, session_id: str = "default"):
    return asyncio.run(run_agent_async(agent, prompt, session_id))