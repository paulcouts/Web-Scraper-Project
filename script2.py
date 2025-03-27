import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

async def main():
    # Minimal prompt: instruct the model to return strictly valid JSON.
    # The JSON must be a single object with a "steps" key whose value is a list of step objects.
    # Each step object must have an "action" key and optionally "url", "selector", or "text".
    # The output must contain no extra text and must end with a final step {"action": "done"}.
    task_instruction = (
        "Return only valid JSON with no extra text. "
        "The JSON must be a single object with a key 'steps' that is a list of step objects. "
        "Each step object must include an 'action' key and, if needed, keys like 'url', 'selector', or 'text'. "
        "Do not output any additional text. Finish with a step {\"action\":\"done\"}. "
        "Task: Navigate to https://www.google.com/maps, click on the 'Directions' button, "
        "set the destination to 'Times Square, New York' (the starting location should be automatically detected as the current location), "
        "and then extract the directions. In the final step, provide a summary of the directions in plain text."
    )

    # Configure the ChatGPT 4o model with strict parameters.
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=512,
        timeout=120,
        max_retries=3,
    )

    # Create the Agent using the task instruction.
    agent = Agent(
        task=task_instruction,
        llm=llm,
    )

    result = await agent.run()
    print("Agent result:", result)

asyncio.run(main())
